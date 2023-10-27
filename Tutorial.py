#This the running program that will teach someone how to code python - but not just code python but use opther tooling and uibld process

print("Hello! Welcome to this python tutorial")
#will need to prompt user for username / password
name = input("what is your name?")
#create an account 
choice = "test"
while choice == "test" :
    choice = input("hello " + name + " - we will need to create an account (type register) or if you all ready have an account - would you like to signin (type login)?")
    #if register - collect username (email address)/ password
    if choice == "login" :
        print("You chose Login")
    elif choice == "register" :
        print("You chose Register")
    else :
        print("Invalid Choice")
        choice = "test"
#if account all ready created error out asking user if they want to reset password

#generate reset code that is 6 random characters/case/numbers

#reset code sent to email address - reset code should have a time to live

#allow user to reset password for specific email address - "set password"

#passwords stored in a file

#location in tutorial is also stored in a file


#should be a terminal like screen that allows for user input

#create files

#run a program 
