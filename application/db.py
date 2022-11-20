import bson

from flask import current_app as app
from . import mongo
from werkzeug.local import LocalProxy

def Signup(email):
    return list(mongo.db.Users.find({"email": email}))

def MakeUser(user):
    return mongo.db.Users.insert_one(user)

def CheckAuth(email):
    return mongo.db.Users.find_one({"email": email})

def GetUserById(id):
    return mongo.db.Users.find_one({"_id": id})