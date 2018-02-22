# CMPT 120 Intro to Programming
# Lab #5 - Working with Strings and Functions
# Author: Willow Duffell
# Created: 2018-02-19

def main():
    
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")

#TODO modify this to generate a Marist-style username
    uname = first + "." + last
    
# ask user to create a new password
    passwd = input("Create new password (minimum of 8 characters): ")

# TODO modify this to ensure the password has at least 8 characters
    while len(passwd) < 8:
        print("Fool of a Took! That password is feeble!")
        print ("The length of the password should be at least 8 characters long")
        passwd = input("Create new password:")  
    
    print("The force is strong with this one...")
    print ("Account configured. Your new email adress is", uname + "@marist.edu")



main()


