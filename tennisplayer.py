#tennisplayer.py

from random import *

class Player:
    def __init__(self, prob):
        self.prob = prob
        self.score = 0
        self.sets = 0
        self.games = 0

    def scorePoint(self):
        # Returns true with probability self.prob
        return random() <= self.prob
    
    def getSets(self):
        return self.sets

    def incScore(self):
        # Add a point to this player's score
        if self.score == 0:
            self.score = 15
        elif self.score == 15:
            self.score = 30
        elif self.score == 30:
            self.score = 40

    def grabScore(self):
        #Return the player's current score
        return self.score

    def gameVictory(self):
        self.games = self.games + 1

    def setVictory(self):
        self.advantage = True

    def noAdvantage(self):
        self.advantage = False

    def advantage(self):
        self.advantage = False

    
        
            


