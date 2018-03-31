from graphics import *
from calc_functions import *

win = GraphWin('Calc', 560, 580)

# Create the text for the display area

eqtdisplayTextElement = Text(Point(0, 15), "")
displayTextElement = Text(Point(15, 75), "")
cols = 7
rows = 6

calcGrid = [
    ['MC', 'M+', 'M-', 'MR', 'MS','sin','cos'],
    ['C','%', '\u221A', 'x\u00b2','1/x','tan','sin^-1'], 
    [7, 8, 9, '+','+/-','cos^-1','tan^-1'],
    [4, 5, 6, '-','log','ln',''],
    [1, 2, 3, '*','10^x','x^y',''],
    ['.', 0,'=','/','(',')','']
]
buttons = [['','','','','','',''],['','','','','','',''],['','','','','','',''],['','','','','','',''],['','','','','','',''],['','','','','','','']]

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
    for i in range(rows):
        for j in range(cols):
            if clicked.getX() > buttons[i][j].p1.getX()and clicked.getX() < buttons[i][j].p2.getX():
                if clicked.getY() > buttons[i][j].p1.getY()and clicked.getY() < buttons[i][j].p2.getY():
                    return i, j
    return -1, -1

def createCalculatorButtons():
    for i in range(rows):
        for j in range(cols):
            buttons[i][j] = calcButton(j * 80, i * 80 + 100, calcGrid[i][j])

def formatResult(theresult):
    resultString = str(theresult)
    if resultString.find('.') > -1:
        resultString = float(resultString)
        resultString= "%.2f" % round(resultString, 2)
    formattedString = str(resultString).rjust(225)
    return formattedString

def evalgroup(groupString):
    if groupString.find('+') > -1:
        mygrouplist = groupString.split("+")
        groupresult = add2numbers(float(mygrouplist[0]), float(mygrouplist[1]))
    elif groupString.find('-') > 0:
        mygrouplist = groupString.split("-")
        groupresult = subtract2numbers (float(mygrouplist[0]), float(mygrouplist[1]))
    elif groupString.find('*') > -1:
        mygrouplist = groupString.split("*")
        groupresult = multiply2numbers (float(mygrouplist[0]), float(mygrouplist[1]))
    elif groupString.find('/') > -1:
        mygrouplist = groupString.split("/")
        groupresult = divide2numbers (float(mygrouplist[0]), float(mygrouplist[1]))
    return groupresult
    
def main():
    memory = 0
    createCalculatorButtons()
    displayString = ''

    eqtdisplayTextElement = Text(Point(0, 15), "")
    eqtdisplayTextElement.draw(win)
    displayTextElement = Text(Point(15, 75), "")
    displayTextElement.draw(win)
    
    xy = False
    xyval=0
    while 1 == 1:
        clicked = win.getMouse()
        print (clicked.getX(), clicked.getY())
        row, col = clickedButton(clicked)
        buttons[row][col].setFill('lavender')
        newstring = str(calcGrid[row][col])
        if  newstring != "=" :
            if newstring == "+/-":
                if displayString != '':
                    result = changesign(float(displayString))
                else:
                    result = "ERROR"
                displayString = formatResult(result)
            elif newstring == "%":
                if displayString != '':
                    result = percent(float(displayString))
                else:
                    result = "ERROR"
                displayString = formatResult(result)
            elif newstring == "\u221A":
                if displayString != '':
                    result = squareroot(float(displayString))
                else:
                    result = "ERROR"
                displayString = formatResult(result)
            elif newstring == "x\u00b2":
                if displayString != '':
                    result = square(float(displayString))
                else:
                    result = "ERROR"
                displayString = formatResult(result)
            elif newstring == "1/x":
                if displayString != '':
                    result = inverse(float(displayString))
                else:
                    result = "ERROR"
                displayString = formatResult(result)
            elif newstring == "C":
                result = ''
                displayString = ''
                xy = False
                xyval = 0
            elif newstring == "sin":
                if displayString != '':
                    result = sin(float(displayString))
                else:
                    result = "ERROR"
                displayString = formatResult(result)
            elif newstring == "cos":
                if displayString != '':
                    result = cos(float(displayString))
                else:
                    result = "ERROR"
                displayString = formatResult(result)
            elif newstring == "tan":
                if displayString != '':
                    result = tan(float(displayString))
                else:
                    result = "ERROR"
                displayString = formatResult(result)
            elif newstring == "sin^-1":
                fdisplay = float(displayString)
                if fdisplay >= -1 and fdisplay <= 1:
                    result = arcsin(float(fdisplay))
                else:
                    result = "ERROR"
                displayString = formatResult(result)
            elif newstring == "cos^-1":
                fdisplay = float(displayString)
                if fdisplay >= -1 and fdisplay <= 1:
                    result = arccos(float(fdisplay))
                else:
                    result = "ERROR"
                displayString = formatResult(result)
            elif newstring == "tan^-1":
                fdisplay = float(displayString)
                if displayString != '':
                    result = arctan(float(fdisplay))
                else:
                    result = "ERROR"
                displayString = formatResult(result)
            elif newstring == "x^y":
                if displayString != '':
                    xy = True
                    xyval = float(displayString)
                    displayString = ''
                else:
                    result = "ERROR"
                    displayString = formatResult(result)
            elif newstring == "10^x":
                if displayString != '':
                    result = tenx(float(displayString))
                else:
                    result = "ERROR"
                displayString = formatResult(result)
            elif newstring == "log":
                if displayString != '':
                    result = log(float(displayString))
                else:
                    result = "ERROR"
                displayString = formatResult(result)
            elif newstring == "ln":
                if displayString != '':
                    result = ln(float(displayString))
                else:
                    result = "ERROR"
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
                displayString = (displayString + str(calcGrid[row][col])).rjust(225);
        else:
            groupopen = displayString.find('(')
            if groupopen > -1:
                groupclose = displayString.find(')')
                if groupclose == -1:
                    displayString + ')'
                    groupclose = displayString.find(')')
                groupstring = displayString[groupopen+1:groupclose]

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
                if xy == True:
                    result = xyfunc(xyval, float(displayString))
                    xy = False
                    xyval = 0
                else:
                    result = "ERROR"
            displayString = formatResult(result)                                 

        eqtdisplayTextElement.undraw()
        eqtdisplayTextElement = Text(Point(0, 15), displayString)
        eqtdisplayTextElement.draw(win)
        displayTextElement.undraw()
        displayTextElement = Text(Point(15, 75), displayString)
        displayTextElement.draw(win)
        print (calcGrid[row][col])
        
        for i in range(rows):
            for j in range(cols):
                if not(i == row and j == col):
                    buttons[i][j].setFill('lightblue')

main()
