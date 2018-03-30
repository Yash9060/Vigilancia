from pymongo import MongoClient
import bson
import os,sys
class mongoDbtest1(object):
	def test(self,Username1,Password1):
		client = MongoClient('localhost', 27017)
		db = client.Users
		UserNames = db.Logindata.find({'Username':Username1, 'Password':Password1})
		if(UserNames.count()==0):
			print("Wrong username password combination")
		else:
			return True