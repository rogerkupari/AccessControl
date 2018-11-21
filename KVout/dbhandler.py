import mysql.connector as my

#yhteystiedot
dbHost = '******'
dbUser = '******'
dbPassword = '******'
dbDatabase = '******'

#Tiedon kirjoittamiselle
dbTable = '******'
dbTableColumn1 = '******'
dbTableColumn2 = '******'

# muuttuja onko db yhteys auki
ConnectionInProcess = False



#vareja
faultCol = '\033[41m'
ordCol = '\033[0m'

# haetaan skannattavat macit tietokannasta
def getMacsFromDb():
	global ConnectionInProcess 
	ConnectionInProcess = True
	print("\nyhdistetaan tietokantaan")
	
	try:
		
		db = my.connect(host=dbHost, user=dbUser, password=dbPassword, database=dbDatabase)
		c = db.cursor()
		qu = ("SELECT mac FROM ruuvit")
		c.execute(qu)
		
		f = open("macs.txt", 'w')
		print("\nhaettu tietokannasta seuraavat macit: ")
		for i in c:
			ii = ''.join(i)
			print(ii)
			f.writelines(ii+"\n")


		c.close()
		f.close()
		db.close()
		ConnectionInProcess = False
	
	except Exception as e:
		print(faultCol+"virhe getMacsFromDb:ssa, tietoja ei haettu, (macs.txt EI PAIVITETTY)" + ordCol)
		print(e)

# Laitetaan tiedot kantaan
def insertDetectedMacIntoDb(dt):
	global ConnectionInProcess
	ConnectionInProcess = True
	print(" \n{rinnakkaisprosessi kaynnissa} Yhdistetaan tietokantaan")
	
	try:
		db = my.connect(host=dbHost, user=dbUser, password=dbPassword, database=dbDatabase)
		c = db.cursor()
		detected = dt

		for i in range(len(detected)):
			
			mc = detected[i][0]
			ts = detected[i][1]
	
			c.execute("""INSERT INTO """ + str(dbTable) + """ ("""+str(dbTableColumn1)+""", """+ str(dbTableColumn2)+""") values('%s', '%s')""" %(mc, ts))
		db.commit()
		c.close()
		db.close()
		print(" \n{rinnakkaisprosessi lakkaa olemasta}Tietokantaan kirjattu seuraavat: \n" +str(detected))
		ConnectionInProcess = False
	except Exception as e:
		#Tahan voi tarvittaessa ottaa tiedostoon kirjoituksen varalle
		print(faultCol+"Tietokantaan kirjoittaminen ei onnistu"+ordCol)
		print(e)