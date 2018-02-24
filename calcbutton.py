from graphics import *
from calc_functions import *

win = GraphWin('Calc', 320, 500)

# Create the text for the display area

displayTextElement = Text(Point(0, 50), "")

calcGrid = [
    [7, 8, 9, '+'],
    [4, 5, 6, '-'],
    [1, 2, 3, '*'],
    ['', 0,'+/-','/'],
    ['', '', '', '=']
]
buttons = [['','','',''],['','','',''],['','','',''],['','','',''],['','','','']]

def calcButton(x, y, value):
    button = Rectangle(Point(x,y),Point(x + 80,y + 80))
    button.setFill('lightblue')
    button.draw(win)
    text = Text(Point(x + 40, y + 40), value)
    text.draw(win)
    return button

def inside(clicked, button):
    if clicked.getX() > button.p1.getX()and clicked.getX() < button.p2.getX():
            if clicked.getY() > button.p1.getY()and clicked.getY() < button.p2.getY():
                return True
    return False

def clickedButton(clicked):
    for i in range(5):
        for j in range(4):
            if clicked.getX() > buttons[i][j].p1.getX()and clicked.getX() < buttons[i][j].p2.getX():
                if clicked.getY() > buttons[i][j].p1.getY()and clicked.getY() < buttons[i][j].p2.getY():
                    return i, j
    return -1, -1

def createCalculatorButtons():
    for i in range(5):
        for j in range(4):
            buttons[i][j] = calcButton(j * 80, i * 80 + 100, calcGrid[i][j])

def main():
    createCalculatorButtons()
    displayString = ''
    displayTextElement = Text(Point(0, 50), "")
    displayTextElement.draw(win)
    while 1 == 1:
        clicked = win.getMouse()
        print (clicked.getX(), clicked.getY())
        row, col = clickedButton(clicked)
        buttons[row][col].setFill('lightgreen')
        newstring = str(calcGrid[row][col])
        if  newstring != "=" :
            displayString = (displayString + str(calcGrid[row][col])).rjust(150);
        else:
            if displayString.find('+') > -1:
                mylist = displayString.split("+")
                result = add2numbers(int(mylist[0]), int(mylist[1]))
            elif displayString.find('-') > -1:
                mylist = displayString.split("-")
                result = subtract2numbers (int(mylist[0]), int(mylist[1]))
            elif displayString.find('*') > -1:
                mylist = displayString.split("*")
                result = multiply2numbers (int(mylist[0]), int(mylist[1]))
            elif displayString.find('/') > -1:
                mylist = displayString.split("/")
                result = divide2numbers (int(mylist[0]), int(mylist[1]))
            else:
                result = "ERROR"
            displayString = str(result).rjust(150)                                   
        displayTextElement.undraw()
        displayTextElement = Text(Point(0, 50), displayString)
        displayTextElement.draw(win)
        print (calcGrid[row][col])
        
        for i in range(5):
            for j in range(4):
                if not(i == row and j == col):
                    buttons[i][j].setFill('lightblue')

main()
