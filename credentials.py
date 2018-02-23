# CMPT 120 Intro to Programming
# Lab #5 - Working with Strings and Functions
# Author: Willow Duffell
# Created: 2018-02-19


def getnames():
    #get user's first and last name
    first = input("Enter your FIRST name: ")
    first = first.lower()
    last = input("Enter your LAST name: ")
    last = last.lower()
    namelist = [first, last]
    return namelist

def buildusername(fname, lname):
    #generate a marist-style username
    uname = fname + "." + lname
    return uname

def entandvalpassword():
    #ask user to create a password
    password = input ("Create a new password (minimum of 8 characters): ")

    while not isPassStrong(password):
        print("Fool of a Took! That password is feeble!")
        password = input("try again.....Create a new password of AT LEAST 8 characters: ")
    return password  
    

def isPassStrong(password):
    #ensure the password has at least 8 characters
    if len(password) < 8:
       return False
    else:
        return True


def main():
    enamelist = getnames()
    uname = buildusername(enamelist[0], enamelist[1])
    passwd = entandvalpassword()

    print("The force is strong with this one...")
    print("Account configured. Your new email address is", uname + "@marist.edu")


main()



