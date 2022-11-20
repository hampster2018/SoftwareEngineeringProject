from flask import current_app as app
from . import mongo

def Signup(email):
    return list(mongo.db.Users.find({"email": email}))

def MakeUser(user):
    return mongo.db.Users.insert_one(user)

def GetByEmail(email):
    return mongo.db.Users.find_one({"email": email})

def GetUserById(id):
    return mongo.db.Users.find_one({"_id": id})

def GetTolls():
    print("I'm here")
    return list(mongo.db.Tolls.find({}))

def UpdateTollByName(name, amount):
    return mongo.db.Tolls.find_one_and_update({'name': name}, {'amount': amount})