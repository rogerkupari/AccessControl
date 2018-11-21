import mysql.connector as my

#vareja
faultCol = '\033[41m'
ordCol = '\033[0m'


#yhteystiedot
dbHost = '******'
dbUser = '******'
dbPassword = '******'
dbDatabase = '******'

#Tiedon kirjoittamiselle
dbTable = '******'
dbTableColumn1 = '******'
dbTableColumn2 = '******'
dbTableColumn3 = '******'

def changeFile(num):
	nm = str(num)
	f = open('id.txt', 'w')
	f.write(nm)
	f.close()

#Hetaan viimeinen indeksitieto
def readFile():
	f = open('id.txt', 'r')
	id = f.read()
	f.close()
	s = int(id)
	return s
	
def cIndex():
	try:
		inId = 0
		outId = 0
		db = my.connect(host=dbHost, user=dbUser, password=dbPassword, database=dbDatabase)
		c = db.cursor(buffered=True)
		incomeid = ("SELECT max(id) FROM income")
		c.execute(incomeid)
		
		for i in c:
			raw = str(i)
			rawToInt = ""
			
			for ii in range(len(raw)):
				if raw[ii].isdigit():
					rawToInt += raw[ii]
					
		inId = int(rawToInt)
		
		outcomeid = ("SELECT max(id) FROM outcome")
		c.execute(outcomeid)
		
		for i in c:
			raw = str(i)
			rawToInt = ""
			
			for ii in range(len(raw)):
				if raw[ii].isdigit():
					rawToInt += raw[ii]
		outId = int(rawToInt)
		
		
		if inId != outId:
			return False
		else:
			return inId

	except Exception as e:
		print(faultCol + "Virhe cIndex():ssa " + ordCol)
		print(e)

def cInsert(dIndex, uIndex):
	try:
		inner = []
		outter = []
		final = []
		dlimit = str(dIndex-1)
		ulimit = str(uIndex-1)
		db = my.connect(host=dbHost, user=dbUser, password=dbPassword, database=dbDatabase)
		c = db.cursor(buffered=True)
		
		inQu = ("SELECT ruuvi, timestamp FROM income WHERE id>'%s' and id<='%s'" %(dlimit, ulimit))
		c.execute(inQu)
		
		for mc, ts in c:
			themac = "{}".format(mc)
			thets = "{}".format(ts)
			temp = themac, thets
			inner.append(temp)
		
		outQu = ("SELECT ruuvi, timestamp FROM outcome WHERE id>'%s' and id<='%s'" %(dlimit, ulimit))
		c.execute(outQu)
		
		for mc, ts in c:
			themac = "{}".format(mc)
			thets = "{}".format(ts)
			temp = themac, thets
			outter.append(temp)
			
		print(outter)
		print(inner)
		
		for i in range(uIndex-dIndex):
			for ii in range(uIndex-dIndex):
				if inner[i][0] == outter[ii][0]:
					res = float(inner[i][1]) - float(outter[ii][1])
					if res < 0:
						print(res)
						print("out")
						c.execute("""insert into direction (direction, mac, ruuvi) values ('out', '%s', (select nimi from ruuvit where ruuvit.mac='%s')) """ % (inner[i][0], inner[i][0]))
					else:
						print(res)
						print("in")
						c.execute("""insert into direction (direction, mac, ruuvi) values ('in', '%s', (select nimi from ruuvit where ruuvit.mac='%s')) """ % (inner[i][0], inner[i][0]))
					outter[ii] = "-----", "-----"
		
		db.commit()
		c.close()
		db.close()
		
		return True
		
	
		
	except Exception as e:
		print(faultCol + "Virhe cInsert():ssa " + ordCol)
		print(e)
		return False
	
	