from pymongo import MongoClient
import bson
import os,sys
class mongoDbtest1(object):
	def test(self,Username1,Password1):
		#client = MongoClient('localhost', 27017)
		#print(serverStatusResult)

		#db = client.Users

		data = bson.decode_file_iter(open(os.getcwd()+'/path/Users/Logindata.bson', 'rb'))

		for u,p in enumerate(data):
			if(p['Username']==Username1 and p['Password']==Password1):
				print("Match found")


			

		#UserNames = db.Logindata.find({'Username':Username1, 'Password':Password1})

		#if(UserNames.count()==0):
			#print("Wrong username password combination")
		#else:
			#should go to main GUI 
			#print("Info Found ")