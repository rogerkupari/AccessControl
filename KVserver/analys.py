import time
import dbhandler as db

loop = True
while(loop):
	#db.changeFile(1)

	lastIndex = db.readFile()

	indexFromDb = db.cIndex()

	if lastIndex != False and indexFromDb != False:
		if indexFromDb != lastIndex:
			inserted = db.cInsert(lastIndex+1, indexFromDb+1)
			
			if inserted == True:
				db.changeFile(indexFromDb)
				
	time.sleep(3)