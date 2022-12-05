from flask import current_app as app
from flask_login import current_user

from bson import ObjectId
from . import mongo
from pymongo import collection

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
    return mongo.db.Users.find_one({"_id": ObjectId(current_user.get_id())})

## Returns the roles given to a user in Array form
def GetRoles():
    return mongo.db.Users.find_one({'_id': ObjectId(current_user.get_id())})['roles']

## Makes a user by passing in a user
def MakeUser(user):
    mongo.db.Users.insert_one(user)

def UpdateUserEmail(email):
    mongo.db.Users.find_one_and_update({'_id': ObjectId(current_user.get_id())}, { '$set': {'email': email}})


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

"""
    Set of functions to report incidents 
"""

ISSUE_TYPES = {
        'Car Crash': 'CC',
        'Traffic Jam': 'TJ',
        'Speed Trap': 'ST',
        'Construction Zone': 'CZ',
        'Hazards': 'HZ',
        'Road Condition': 'RC'
    }

def GetIssues():
    collection = mongo.db.get_collection("Issues")
    Issues = collection.aggregate( { '$sort': { 'date': 1}})
    return Issues

def GetIssue(issueType, issueNumber):
    issueName = IssueNameUtil(issueType, issueNumber)
    return mongo.db.Issues.find_one({'name': issueName})

def GetNextIssueName(issueType):
    currentNum = mongo.db.NumIssueOfType.find_one({'type': issueType})
    if currentNum is None:
        mongo.db.NumIssueOfType.insert_one({'type': issueType, 'number': 1})
        num = 1
    else: 
        num = currentNum['number'] + 1
    acronym = ISSUE_TYPES.setdefault(issueType, 'Unknown Issue')
    return (acronym + str(num)), num 

def MakeIssue(issueType, latitude, longitude, description):
    issueName, currentNumber = GetNextIssueName(issueType=issueType)
    mongo.db.Issues.insert_one({'name': issueName, 'type': issueType, 'lat': latitude, 'long': longitude, 'description': description})
    UpdateNextIssueNum(issueType, currentNumber)

def UpdateNextIssueNum(issueType, num):
    mongo.db.NumIssueOfType.find_one_and_update({'type': issueType}, { '$set': { 'number': num }})

def IssueNameUtil(issueType, num):
    return ISSUE_TYPES.setdefault(issueType, 'Unknown Type') + str(num)