
import os
import hashlib


#import pytest
#import mock
#import builtins


def greet():
    print("Hello! Welcome to this python tutorial")
    greeting = input("what is your name?")
    return greeting

def readFile():
    d = {}
    i = 0
    with open('temp/usernames.txt','r') as temp_file:
        for line in temp_file:  
            lined = {}
            (name, email, password) = line.split(',')
            name = name.split(': ')[1]
            lined['name'] = name
            print("Name:" + name)
            email = email.split(': ')[1]
            lined['email'] = email
            print("Email:" + email)
            password = password.split(': ')[1]
            lined['password'] = password
            print("Password:" + password)
            d[i] = lined
            i+=1
            print(d)
    temp_file.close()
    return d

def findUser(usersDict, userEmail):
    status = False
    i=0
    ##Need to think of a way to exit out when found - userFound or end of Dict
    for user in usersDict:
        userDict = usersDict[user]
        for key in userDict:
            #print(str(i) + "---" + key + ": " + userDict[key])
            if userDict['email'] == userEmail:
                status=True
        i+=1
    return status

def validateUser(usersDict, userEmail, userPassword):
    status = False
    i=0
    ##Need to think of a way to exit out when found - userFound or end of Dict
    for user in usersDict:
        userDict = usersDict[user]
        for key in userDict:
            #print(str(i) + "---" + key + ": " + userDict[key])
            if userDict['email'] == userEmail and userDict['password'] == userPassword:
                status=True
        i+=1
    return status

def updateFile(usersDict):
    status = False
    i=0
    for user in usersDict:
        userDict = usersDict[user]
        for key in userDict:
            print(str(i) + "---" + key + ": " + userDict[key])
        i+=1
    return status

def login():
    status = False
    return status


def registerUser(usersDict, userName, userEmail, userPassword):
    status = False

    
    if findUser(usersDict, userEmail):
            print("User all ready exists")    
        
        
    else:
        print("User is going to be registered")
        status=True
        #add user to the file
        with open('temp/usernames.txt','a') as temp_file:
            temp_file.write("name: " + userName + ", email: " + userEmail + ", password: " + userPassword + "\n")
        temp_file.close()
    return status


