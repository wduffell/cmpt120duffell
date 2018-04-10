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

emotionMatrix = [
    [4, 0, 0, 2],
    [2, 0, 0, 2], 
    [2, 3, 5, 2],
    [2, 3, 3, 2],
    [2, 3, 5, 2],
    [4, 3, 5, 2]
]

feelingslist = ["anger", "disgust", "happiness", "sadness", "surprise", "fear"]
actionslist = ["reward", "punish", "threaten", "joke"]
reactionlist = ["Grrr! That made me angry!", "Yuck! that is disgusting", "Wooohooo! that made me happy", "Boohoo, you are going to make me cry", "Wow! Very Surprising",  "Now I'm scared"]


def introduction():
    print("Hi I'm AI, my name is AL")
    emotion = random.choice(feelingslist)
    indexfeeling = feelingslist.index(emotion)
    print("Today I'm feeling: " + emotion)
    return indexfeeling

def getInteraction():
    userAction = input("What do you want to do to Al? (Type either reward, punish, joke or threaten): ")
    try:
        userAction = actionslist.index(userAction)
    except:
        userAction = 4
    return userAction
    
    
def lookupEmotion(currEmotion, userAction):

    newemotion = emotionMatrix[currEmotion][userAction]
    return newemotion

def main():
    goonforever = True
    currEmotion = introduction()
    while goonforever == True:
        userAction = getInteraction()
        if userAction == 4:
            print("Invalid Action")
            print('\n')
            continue
        else:
            currEmotion = lookupEmotion(currEmotion, userAction)
            print(reactionlist[currEmotion])
            print('\n')
    return

main()

    
