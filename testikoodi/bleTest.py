import subprocess, time, os, signal

komento = "sudo hcitool scan"
komento2 = "sudo hcitool lescan"
jat = True
tiedo = False
while(jat):
        btsch = subprocess.Popen((komento).split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        time.sleep(2)
        btsch.kill()
        data1, error1  = btsch.communicate()
	blesch = subprocess.Popen((komento2).split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        time.sleep(2)
       	os.kill(blesch.pid, signal.SIGINT)
	data2, error2 =  blesch.communicate()
	data = data1 + data2
	error = error1 + error2
        if error:
                print(error)
                os.system("sudo hciconfig hci0 down")
                time.sleep(1)
                os.system("sudo hciconfig hci0 up")
                time.sleep(1)
        else:
                if tiedo == False:
                        file = open('teksti.txt', 'r')
                        tark = file.readlines()
                        file.close()
                        tiedo = True

                yks = str(tark[0]).strip('\n')
                kaks = str(tark[1]).strip('\n')
		kol = str(tark[2]).strip('\n')		

               # print(yks in data)
               # print(kaks in data)
		#print(kol in data)
		if yks in data:
			print('iphone online')
		if kaks in data:
			print('kone online')
		if kol in data:
			print('ruuvi online')
		else:
			continue
		#print(data)
		
