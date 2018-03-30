# CMPT 120 Intro to Programming
# Lab #6 – Lists and Error Handling
# Author: Willow Duffell
# Created: 2018-03-26

symbol = [ " ", "x", "o" ]

#def printRow(row):   
   
def printBoard(board):
    print("+-----------+")
    print("| ",board[6],"| ",board[7],"| ",board[8],"|")
    print("+-----------+")
    print("| ",board[3],"| ",board[4],"| ",board[5],"|")
    print("+-----------+")
    print("| ",board[0],"| ",board[1],"| ",board[2],"|")
    print("+-----------+")

printBoard(['','','','','','','','',''])

#def markBoard(board, row, col, player):
   # if board == '':
   # else:
        #print("Sorry you can't go there")
# check to see whether the desired square is blank
# if so, set it to the player number
#pass

#def getPlayerMove():
#input("") # prompt the user separately for the row and column numbers
#return (0,0) # then return that row and column instead of (0,0)

#def hasBlanks(board):
# for each row in the board...
# for each square in the row...
# check whether the square is blank
# if so, return True
#return True # if no square is blank, return False

def main():
    board = [
        ['0','0','0'],
        ['0','0','0'],
        ['0','0','0']
        ] # TODO replace this with a three-by-three matrix of zeros
    player = 1
    while hasBlanks(board):
        printBoard(board)
        row,col = getPlayerMove()
        markBoard(board,row,col,player)
        player = player % 2 + 1 # switch player for next turn






main()