from graphics import *
from calc_functions import *

win = GraphWin('Calc', 480, 660)



cols = 6
rows = 7

calcGrid = [
    ['MC', 'M+', 'M-', 'MR', 'MS', ''],
    ['sin', 'sin^-1', 'cos', 'cos^-1', 'tan', 'tan^-1'],
    ['+/-', '\u221A', 'x\u00b2', '1/x','10^x','ln'], 
    ['C',7, 8, 9, '+','x^y'],
    ['CE',4, 5, 6, '-','%'],
    ['',1, 2, 3, '*',')'],
    ['','.', 0,'=','/','(']
]
buttons = [['','','','','','',''],['','','','','','',''],['','','','','','',''],['','','','','','',''],['','','','','','',''],['','','','','','',''],['','','','','','','']]

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

def undrawDisplays():
    eqtdisplayTextElement.draw(win)
    displayTextElement.draw(win)
    
def formatResult(theresult):
    resultString = str(theresult)
    #if resultString.find('.') > -1:
    #    resultString = float(resultString)
    #    resultString= "%.2f" % round(resultString, 2)
    formattedString = str(resultString).rjust(200)
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



def memorybuttonpressed(newstring, memory, displayString):

    if newstring == "MC":
        memory = 0
        result = displayString
         
    elif newstring == "MR":
        result = memory

    elif newstring == "MS":
        memory = displayString
        result = displayString

    elif newstring == "M+":
        result = add2numbers(float(memory), float(displayString))

    elif newstring == "M-":
        result = subtract2numbers (float(memory), float(displayString))
       
    return memory, result

def calculateresult(displayString, eqtdisplayString):

    evalString = eqtdisplayString + displayString

    if evalString.find('+') > -1:
        mylist = evalString.split("+")
        result = add2numbers(float(mylist[0]), float(mylist[1]))
    elif evalString.find('-') > 0:
        mylist = evalString.split("-")
        result = subtract2numbers (float(mylist[0]), float(mylist[1]))
    elif evalString.find('*') > -1:
        mylist = evalString.split("*")
        result = multiply2numbers (float(mylist[0]), float(mylist[1]))
    elif evalString.find('/') > -1:
        mylist = evalString.split("/")
        result = divide2numbers (float(mylist[0]), float(mylist[1]))
    elif evalString.find('x^y') > -1:
        result = xyfunc(xyval, float(displayString))

    displayString = formatResult(result)
    return displayString, eqtdisplayString

def advancedbuttons(newstring, displayString):
    print("newstring = " + newstring)
    print("displayString = " + displayString)

    if newstring == "+/-":
        result = changesign(float(displayString))
    elif newstring == "%":
        result = percent(float(displayString))
    elif newstring == "\u221A":
        result = squareroot(float(displayString))
    elif newstring == "x\u00b2":
        result = square(float(displayString))
    elif newstring == "1/x":
        result = inverse(float(displayString))
    elif newstring == "sin":
        result = sin(float(displayString))
    elif newstring == "cos":
        result = cos(float(displayString))
    elif newstring == "tan":
        result = tan(float(displayString))
    elif newstring == "sin^-1":
        fdisplay = float(displayString)
        if fdisplay >= -1 and fdisplay <= 1:
            result = arcsin(float(fdisplay))
        else:
            result = "0"
    elif newstring == "cos^-1":
        fdisplay = float(displayString)
        if fdisplay >= -1 and fdisplay <= 1:
            result = arccos(float(fdisplay))
        else:
            result = "0"
    elif newstring == "tan^-1":
        result = arctan(float(displayString))
    elif newstring == "10^x":
        result = tenx(float(displayString))
    elif newstring == "log":
        result = log(float(displayString))
    elif newstring == "ln":
        result = ln(float(displayString))

    result = "%.4f" % round(float(result), 2)
    return result

def calculategroup(grp, disp, eqtdisp):
    i = eqtdisp.rfind('(')
    print(mystring)
    newstring = eqtdisp[i+1:]
    print(newstring)
    newstring = newstring.rstrip(')')
    disp = calculateresult(newstring, eqtdisp)
    return disp, eqtdisp

    
def main():
    memory = 0
    createCalculatorButtons()
    displayString = '0'
    eqtdisplayString = ''
    group = 0

    cleardisplay = False

    myeqtTextString = str(eqtdisplayString).rjust(200)
    eqtdisplayTextElement = Text(Point(0, 15), myeqtTextString)
    eqtdisplayTextElement.draw(win)

    myTextString = str(displayString).rjust(200)
    displayTextElement = Text(Point(15, 75), myTextString)
    displayTextElement.draw(win)

    while 1 == 1:
        clicked = win.getMouse()
        print (clicked.getX(), clicked.getY())
        row, col = clickedButton(clicked)
        buttons[row][col].setFill('lavender')
        newstring = str(calcGrid[row][col])
        #check to make sure they didn't click on an empty square
        if newstring == '':
            continue
    
        if row == 0 : # Memory buttons
            memory, displayString = memorybuttonpressed(newstring, memory, displayString)
         
        elif row == 1 or row == 2: #advanced calculator buttons that will return a result if not a group
            displayString  = advancedbuttons(newstring, displayString)

        elif newstring == "C":
            result = '0'
            displayString = '0'
            eqtdisplayString = ''
            group = 0

        elif newstring == "CE":
            displayString = '0'
            result = '0'

        else: # primary calculator buttons
            if newstring.isdigit() == True: #number pressed
                if displayString == '0':
                    displayString = newstring
                elif cleardisplay == True:
                    displayString = newstring
                    cleardisplay = False
                else:
                    displayString = displayString + newstring
            elif newstring == '(':
                group = group + 1
                if displayString == '0':
                    displayString = ''
                eqtdisplayString = eqtdisplayString + newstring
            elif newstring == ')':
                #check to make sure there was a '(' first
                if group <= 0:
                    continue
                eqtdisplayString = eqtdisplayString + newstring
                #calculate
                displayString = calculategroup(group, displayString, eqtdisplayString)
                #print("EqtDisplatString:" + eqtdisplayString)
                #print("DisplayString: " + displayString)
                
            else: # something besides a number or group
                if  newstring != "=" : #something besides =
                    print("EqtDisplayString: " + eqtdisplayString)
                    print("DisplayString: " + displayString)

                    
                    if newstring == ".":
                        displayString = displayString + newstring
                    else:
                        cleardisplay = True
                        if eqtdisplayString == '':
                            eqtdisplayString = displayString
                        eqtdisplayString  = eqtdisplayString + newstring
                        
                else: #calculate
                    cleardisplay = True
                    displayString, eqtdisplayString = calculateresult(displayString, eqtdisplayString)
                    eqtdisplayString = ""
       
        myeqtTextString = formatResult(eqtdisplayString)
        eqtdisplayTextElement.undraw()
        eqtdisplayTextElement = Text(Point(0, 15), myeqtTextString)
        eqtdisplayTextElement.draw(win)

        myTextString = formatResult(displayString)
        displayTextElement.undraw()
        displayTextElement = Text(Point(15, 75), myTextString)
        displayTextElement.draw(win)

        for i in range(rows):
            for j in range(cols):
                if not(i == row and j == col):
                    buttons[i][j].setFill('lightblue') 
        

main()
