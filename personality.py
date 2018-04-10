#personality.py
#Intro to Programming
#Author: Willow Duffell
#Date: 4-9-18


#feelings
#0 = "anger"
#1 = "disgust"
#2 = "happiness"
#3 = "sadness"
#4 = "surprise"
#5 = "fear"

#0 = "reward"
#1 = "punish"
#2 = "threaten"
#3 = "joke"
import random
feelingslist = ["anger", "disgust", "happiness", "sadness", "surprise", "fear"]
actionslist = ["reward", "punish", "threaten", "joke"]
#Make a table
def introduction():
    print("Hi I'm Al")
    print("Today I'm feeling:" + random.choice(feelingslist))
# Get the mode of interaction from the user
# Params: none
# Returns: an integer indicating one of reward, punish, joke, or threaten
def getInteraction():
    action = input("What do you want to do to Al? (Type either reward, punish, joke or threaten): ")
    if action == "reward":
        return 0
    elif action == "punish":
        return 1
    elif action == "threaten":
        return 2
    elif action == "joke":
        return 3
    else:
        return 4
    
        
    
# Based on a given emotion and action, determine the next emotional state
# Params:
# currEmotion - a current emotion
# userAction - a user interaction
# Returns: an emotion
def lookupEmotion(currEmotion, userAction):
#pass # TODO do the matrix lookup
    return 0 # return an integer corresponding to an emotion


def main():
    goonforever = True
    introduction()
    while goonforever == True:
        returnedaction = getInteraction()
        if returnedaction == 4:
            print("Invalid Action")
            continue
        else:
            print("Action = " + actionslist[returnedaction])
    return

main()
    

    
