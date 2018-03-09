from graphics import *
from calc_functions import *

win = GraphWin('Calc', 400, 580)

# Create the text for the display area

displayTextElement = Text(Point(0, 50), "")

calcGrid = [
    ['MC', 'M+', 'M-', 'MR', 'MS'],
    ['C','%', '\u221A', 'x\u00b2','1/x'], 
    [7, 8, 9, '+','+/-'],
    [4, 5, 6, '-',''],
    [1, 2, 3, '*',''],
    ['.', 0,'=','/','']
]
buttons = [['','','','',''],['','','','',''],['','','','',''],['','','','',''],['','','','',''],['','','','','']]

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
    for i in range(6):
        for j in range(5):
            if clicked.getX() > buttons[i][j].p1.getX()and clicked.getX() < buttons[i][j].p2.getX():
                if clicked.getY() > buttons[i][j].p1.getY()and clicked.getY() < buttons[i][j].p2.getY():
                    return i, j
    return -1, -1

def createCalculatorButtons():
    for i in range(6):
        for j in range(5):
            buttons[i][j] = calcButton(j * 80, i * 80 + 100, calcGrid[i][j])

def formatResult(theresult):
    resultString = str(theresult)
    if resultString.find('.') > -1:
        resultString = float(resultString)
        resultString= "%.2f" % round(resultString, 2)
        formattedString = str(resultString).rjust(150)
    else:
        formattedString = str(resultString).rjust(150)
    return formattedString
    
def main():
    memory = 0
    createCalculatorButtons()
    displayString = ''
    displayTextElement = Text(Point(0, 50), "")
    displayTextElement.draw(win)
    while 1 == 1:
        clicked = win.getMouse()
        print (clicked.getX(), clicked.getY())
        row, col = clickedButton(clicked)
        buttons[row][col].setFill('lavender')
        newstring = str(calcGrid[row][col])
        if  newstring != "=" :
            if newstring == "+/-":
                result = changesign(float(displayString))
                displayString = formatResult(result)
            elif newstring == "%":
                result = percent(float(displayString))
                displayString = formatResult(result)
            elif newstring == "\u221A":
                result = squareroot(float(displayString))
                displayString = formatResult(result)
            elif newstring == "x\u00b2":
                result = square(float(displayString))
                displayString = formatResult(result)
            elif newstring == "1/x":
                result = inverse(float(displayString))
                displayString = formatResult(result)
            elif newstring == "C":
                result = ""
                displayString = formatResult(result)
            elif newstring == "MC":
                memory = 0
            elif newstring == "MR":
                result = memory
                displayString = formatResult(result)
            elif newstring == "MS":
                if (displayString != ""):
                    memory = displayString
                result = ""
                displayString = formatResult(result)
            elif newstring == "M+":
                if displayString == "":
                    mem = 0
                else:
                    mem = displayString
                result = add2numbers(float(memory), float(mem))
                displayString = formatResult(result)
            elif newstring == "M-":
                if displayString == "":
                    mem = 0
                else:
                    mem = displayString
                result = subtract2numbers (float(memory), float(mem))
                displayString = formatResult(result)
            else:
                displayString = (displayString + str(calcGrid[row][col])).rjust(150);
        else:
            if displayString.find('+') > -1:
                mylist = displayString.split("+")
                result = add2numbers(float(mylist[0]), float(mylist[1]))
            elif displayString.find('-') > 0:
                mylist = displayString.split("-")
                result = subtract2numbers (float(mylist[0]), float(mylist[1]))
            elif displayString.find('*') > -1:
                mylist = displayString.split("*")
                result = multiply2numbers (float(mylist[0]), float(mylist[1]))
            elif displayString.find('/') > -1:
                mylist = displayString.split("/")
                result = divide2numbers (float(mylist[0]), float(mylist[1]))
            else:
                result = "ERROR"
            displayString = formatResult(result)                                 
        displayTextElement.undraw()
        displayTextElement = Text(Point(0, 50), displayString)
        displayTextElement.draw(win)
        print (calcGrid[row][col])
        
        for i in range(6):
            for j in range(5):
                if not(i == row and j == col):
                    buttons[i][j].setFill('lightblue')

main()
