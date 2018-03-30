"""Class for connecting and using MongoDB functionality."""
from pymongo import MongoClient
import bson
import os,sys

class MongoDBClient(object):
    def __init__(self):
        self.client = MongoClient('localhost', 27017)

    def verify_username_and_password(self, uname, passwd):
        db = self.client.Users
        UserNames = db.Logindata.find(
            {'Username':uname, 'Password':passwd})
        return UserNames.count() > 0
