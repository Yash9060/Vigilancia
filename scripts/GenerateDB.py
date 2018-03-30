"""This file initializes Mongo Db database with initial data and should be
executed only once per system. Make sure that Mongo Db server is running on
local host before executing this file .
"""

from pymongo import MongoClient
import sys, os

if __name__ == '__main__':
    client = MongoClient('localhost', 27017)

    db = client.Users
    Username = ['admin', 'system']
    Password = ['admin', 'admin']

    print("Generating username and password database entries...")
    for i in range(len(Username)):
        User = {
            'Username': Username[i],
            'Password':Password[i]
        }
        result=db.Logindata.insert_one(User)

    print("Database entries generated successfully.")
