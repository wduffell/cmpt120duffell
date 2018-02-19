# CMPT 120 Intro to Programming
# Lab #5 - Working with Strings and Functions
# Author: Willow Duffell
# Created: 2018-02-19

def main():

# get user's first and last name
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")

# TODO modify this to generate a Marist-style username
    uname = first + last

# ask user to create a new password
    passwd = input("Create new password: ")

# TODO modify this to ensure the password has at least 8 characters
    while False:
        print ("Fool of a Took! That password is feeble!")
        passwd = input("Create new password: ")
        print("The force is strong with this one...")
        print ("Account configured. Your new email adress is", uname + "@marist.edu")
    

main()    
