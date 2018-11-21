#coding=utf-8

import subprocess, time, os, signal
import threading
import time
import dbhandler


# ble aktiiviseen skannaukseen kaytettava aika + komento subprocessiin
scantime = 3
scancommand = "sudo hcitool lescan"



#haetaan skannattavat macit "pysyvasta" tiedostosta
def getmac():
	if dbhandler.ConnectionInProcess:
		print(dbhandler.faultCol + "tietokantayhteys auki ennestaan, yhteytta ei voida muodostaa, odotetaan" + dbhandler.ordCol)
		while dbhandler.ConnectionInProcess:
			time.sleep(1)
	else:
		dbhandler.getMacsFromDb()
		#print("<-- luetaan mac osoitteita kayttotiedostosta -->")	
		f = open("macs.txt", 'r')
		sc = f.readlines()
		f.close()	
		return sc
		#print("<----------------- valmis --------------------->")



#skannataan
def getrc():
	#print("<-- ble skannaus -->")
	btsch = subprocess.Popen((scancommand).split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        time.sleep(scantime)
        os.kill(btsch.pid, signal.SIGINT)
        data, error  = btsch.communicate()
        if error:
                print(error)
                os.system("sudo hciconfig hci0 down")
                time.sleep(1)
                os.system("sudo hciconfig hci0 up")
                time.sleep(1)
                print("bt-moduuli kaynnistetty uudelleen")
        else:
		return data



loop = True

#haetaan macit kaynnistyksen yhteydessa
getmacs = False

#lahetysjono ja lahtevat + lahetetyt
sbuff = []
send = []

# lahetettyjen rivien maara (apumuuttuja)
sendListLen = 0
#lupa lahetykselle pitaa olla tassa kohtaa true
sflag = True

while(loop):

	#jos macceja ei ole haettu (ja kun ei ole), ne haetaan kaynnistyksen yhteydessa
	if not getmacs:
		macstemp = getmac()
		while macstemp == None:
			macstemp = getmac()
		print("------------------    skannattavat macit paivitetty tiedostoon:    ------------\n")
		print(macstemp)
		print("\n-------------------------------------------------------------------------------")
		getmacs = True
                
	else:
		#skannataan niin kauan kunnes saadaan data
		data = getrc()
		while data == None:
			data = getrc()
		
		# send listan tyhjennys jos db yhteydet sulki, lahetettya dataa on, eika ole viela lupaa lahettaa uusia -> tyhjennetaan lahetetyt ja annetaan lupa lahetykseen
		if dbhandler.ConnectionInProcess == False and sendListLen >> 0 and sflag == False:
				del send[0:sendListLen]
				sflag = True

		# tarkastetaan tietokannasta haettuja macceja datalta
		for i in range(len(macstemp)):
			test = str(macstemp[i]).strip('\n')
			if test in data:
					if test not in sbuff and test not in send:
						sbuff.append(test)
						print("tagi: %s laitettu lahetysjonoon" % (str(test)))
				
			# jos ei datalla mutta ollut siella (sbuff) eika ole viela lahetetty -> lisataan jonoon odottamaan
			else:
					if test in sbuff and test not in send:
						tempTime = time.time()
						tempToSend = str(macstemp[i].strip('\n')), str(tempTime)
						send.append(tempToSend)
						sbuff.remove(test)
						print("tagi: %s poistettu lahetysjonosta" % (str(test)))
						print("tagi %s valmistellaan lahetykseen aikaleimalla %s" % (send[-1][0], send[-1][1]))
						
				
		# jos send listalla on tavaraa ja aikaisemmat db yhteydet on sulki, eika kyseista tietoa ole viela lahetetty -> lahetetaan
		if len(send) >> 0 and dbhandler.ConnectionInProcess == False and sflag == True:
			sendListLen = len(send)
			writedb = threading.Thread(target=dbhandler.insertDetectedMacIntoDb, args=(send,))
			writedb.start()
			print("Seuraavat tiedot toimitettu lahetettavaksi: \n" + str(send))
			sflag = False
