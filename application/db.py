from flask import current_app as app
from flask_login import current_user

from bson import ObjectId
from . import mongo

"""
    Set of functions to create and get User information
"""
## Returns a user or None by the email
def GetUserByEmail(email):
    return mongo.db.Users.find_one({"email": email})

## Returns a user or None by the id for loading_user function
def GetById(id):
    return mongo.db.Users.find_one({"_id": id})

def GetUserById():
    return mongo.db.Users.find_one({"_id": current_user.get_id()})

## Returns the roles given to a user in Array form
def GetRoles():
    return mongo.db.Users.find_one({'_id': ObjectId(current_user.get_id())})['roles']

## Makes a user by passing in a user
def MakeUser(user):
    mongo.db.Users.insert_one(user)


"""
    Set of functions to get and make issues for users
"""
def GetIssues():
    return mongo.db.Issues.find_one({'_id': ObjectId(current_user.get_id())})

def MakeIssue(Issue):
    user = GetIssues()
    if user is not None:
        issues = user['Issues']
        issues.append(Issue)
        mongo.db.Issues.find_one_and_update({'_id': ObjectId(current_user.get_id())}, { '$set': {'Issues': [issues]}})
    else:
        mongo.db.Issues.insert_one({'_id': ObjectId(current_user.get_id()), 'Issues': [Issue]})
        

"""
    Set of functions to get and update Tolls
"""
def GetTolls():
    return list(mongo.db.Tolls.find({}))

def SetTollByName(name, amount):
    return mongo.db.Tolls.find_one_and_update({'name': name}, {'amount': amount})