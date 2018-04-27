#tennismatch.py

from player import Player

class TennisMatch:
    def __init__(self, probA, probB):
        self.playerA = Player(probA)
        self.playerB = Player(probB)
        self.server = self.playerA
        self.acceptor = self.playerB

    def play(self):
        if self.server.scorePoint():
            if self.server.grabScore()== 40 and self.acceptor.grabScore() == 40:
                if self.server.hasAdvantage():
                    self.server.gameVictory()
                    if self.server.games >= 6 and self.server.games - self.acceptor.games >= 2:
                        self.server.setVictory()
                        self.acceptor.resetScore()
                        self.server.changeServer()
                elif self.acceptor.hasAdvantage():
                    self.acceptor.noAdvantage():
                else:
                    self.server.advantage()
                    

            elif self.server.grabScore() == 40 and self.acceptor.grabScore() < 40:
                self.server.gameVictory()
                if self.server.games >= 6 and self.server.games - self.acceptor.games >= 2:
                    self.server.setVictory()
                self.acceptor.resetScore()
                self.server.resetScore()
                self.server.changeServer()
            else:
                self.server.incScore()

        else:
            self.acceptor.incScore()
            if self.acceptor.grabScore() == 40 and self.server.grabScore() < 40:
                self.acceptor.gameVictory()
                if self.acceptor.games >= 6 and self.acceptor.games - self.server.games >= 2:
                    self.acceptor.setVictory()
                self.server.resetScore()
                self.acceptor.resetScore()
                self.server.changeServer()
            

    def grabScores(self):
        return self.playerA.grabScore(), self.playerB.grabScore()

    def isOver(self):
        if self.playerA.getSets() == 3 or self.playerB.getSets() == 3:
        

    def changeServer(self):
        if self.server == self.playerA:
            self.server = self.playerB
            self.acceptor = self.playerA
        else:
            self.server = self.playerA
            self.acceptor = self.playerB

