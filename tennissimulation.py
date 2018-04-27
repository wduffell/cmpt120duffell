#tennissimulation.py

from simstats import SimStats
from tennismatch import TennisMatch


def printIntro():
    print("This program simulates a game of tennis between two")
    print('players called "A" and "B". The abilities of each player is')
    print("indicated by a probability (a number between 0 and 1)")

def getInputs():
    probA = float(input("What is the prob. player A wins a serve? "))
    probB = float(input("What is the prob. player B wins a serve? "))
    n = int(input("How many games to simulate? "))
    return probA, probB, n

def main():
    printIntro()
    probA, probB, n = getInputs()
    stats = SimStats()
    for i in range(n):
        theGame = TennisMatch(probA, probB)
        theGame.play()
        stats.update(theGame)
    stats.printReport()
   

main()
