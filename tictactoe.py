# CMPT 120 Intro to Programming
# Lab #6 – Lists and Error Handling
# Author: Willow Duffell
# Created: 2018-03-26

symbol = [ " ", "x", "o" ]
board = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
        ] 

def printRow(row):
  
    output =  "| "
    for i in range(3):
        value = board[row][i]
        if value == 0:
            value = symbol[0]
        elif value == 1:
            value = symbol[1]
        elif value == 2:
            value = symbol[2]
        output = output + str(value) + " | "
    
    print(output)
   
def printBoard(board):
    for i in range(3):
        print("+-----------+")
        printRow(i)
    print("+-----------+")
    

def markBoard(board, row, col, theplayer):
   
    if board[row][col] == 0:
        if theplayer == 1:
            board[row][col] = 1
        else:
            board[row][col] = 2
        return True
    else:
        print("That space is taken - Try again");
        return False
        
def printBoardDebug(board):

    output =  str(board[0][0]) + ',' +  str(board[0][1]) + ',' + str(board[0][2])
    print(output)
    output =  str(board[1][0]) + ',' +  str(board[1][1]) + ',' + str(board[1][2])
    print(output)
    output =  str(board[2][0]) + ',' +  str(board[2][1]) + ',' + str(board[2][2])
    print(output)

    
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
    player = 1
    printBoard(board)
    while 1:
        if player == 1:
            playerstring = "Player 1"
            currentplayer = 1;
            player =2
        else:
            playerstring = "Player 2"
            currentplayer = 2
            player = 1
        playerrow = input(playerstring +" - Pick where you want to go. Select a row 1-3: ")
        playercol = input("Now pick a column 1, 2, or 3: ")
        
        playerrow = int(playerrow)-1
        playercol = int(playercol)-1
        if markBoard(board, int(playerrow),int(playercol),int(currentplayer)) == False:
            player = currentplayer
        printBoard(board)               
    #while hasBlanks(board):
    #row,col = getPlayerMove()
    #markBoard(board,row,col,player)
    #player = player % 2 + 1 # switch player for next turn

main()
