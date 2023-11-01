
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



if not os.path.exists("temp") :
    os.mkdir("temp")

print("This is a test")

print(os.listdir())

#os.system('touch usernames.txt')
#temp_file = open('temp/usernames.txt','a')


#This the running program that will teach someone how to code python - but not just code python but use opther tooling and uibld process


#get users name
greeting = greet()

usersDict = readFile()


#will need to prompt user for username / password
#create an account 
choice = "test"
while choice == "test" :
    choice = input("hello " + greeting + " - we will need to create an account (type register) or if you all ready have an account - would you like to signin (type login)?")
    #if register - collect username (email address)/ password
    if choice == "login" :
        print("You chose Login")
    elif choice == "register" :
        print("You chose Register")
    else :
        print("Invalid Choice")
        choice = "test"

if choice == "register" :
    email = input("Thanks " + greeting + " please provide your email address:")
    #if account all ready created error out asking user if they want to reset password
    #if(email)
    passwordInvalid = True

    while passwordInvalid :
        password = input("Thanks " + greeting + " please provide a password (you will be prompted a second time):")
        password2 = input("Thanks " + greeting + " retype password:")
        if(password == password2) :
            passwordInvalid = False
            passwordSha = hashlib.new('sha3_512')
            password = password.encode('utf-8')
            passwordSha.update(password)
            status = registerUser(usersDict, greeting, email, str(passwordSha.digest()))
            if status:
                print("Zach says " + str(status))
                usersDict = readFile()

            else:
                print("Zachary says " + str(status))
        else :
            print("The passwords do not match or do not minimum criteria please try again.")
    #store the username and password in a file
    print("Thank you " + greeting + " you will now be asked to login.")

#temp_file.close()

#generate reset code that is 6 random characters/case/numbers

#reset code sent to email address - reset code should have a time to live

#allow user to reset password for specific email address - "set password"

#passwords stored in a file

#location in tutorial is also stored in a file


#should be a terminal like screen that allows for user input

#create files

#run a program 
