#tennismatch.py

from player import Player

class TennisMatch:
    def __init__(self, probA, probB):
        self.playerA = Player(probA)
        self.playerB = Player(probB)
        self.server = self.playerA

    def play(self):
        while not self.isOver():
            if self.server.winsServe():
                self.server.incScore()
            else:
                self.changeServer()

    def getScores(self):
        return self.playerA.getScore(), self.playerB.getScore()

    def isOver(self):
        return self.playerA.getScore() == 15 or self.playerB.getScore() == 15 \
            or (self.playerA.getScore() == 7 and self.playerB.getScore() == 0) \
            or (self.playerB.getScore() == 7 and self.playerA.getScore() == 0)

    def changeServer(self):
        if self.server == self.playerA:
            self.server = self.playerB
        else:
            self.server = self.playerA

