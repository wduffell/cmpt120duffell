from graphics import *
from calc_functions import *

win = GraphWin('Calc', 480, 660)

cols = 6
rows = 7

calcGrid = [
    ['MC', 'M+', 'M-', 'MR', 'MS', 'Quit'],
    ['sin', 'sin^-1', 'cos', 'cos^-1', 'tan', 'tan^-1'],
    ['+/-', '\u221A', 'x\u00b2', '1/x','10^x','ln'], 
    ['C',7, 8, 9, '+','x^y'],
    ['CE',4, 5, 6, '-','%'],
    ['',1, 2, 3, '*',')'],
    ['','.', 0,'=','/','(']
]

class Button:

    def __init__(self, win, center, width, height, label):
        w,h = width/2.0, height/2.0
        x,y = center.getX(),center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1, p2)
        self.rect.setFill('lavender')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def activate(self):
        "Sets this button to 'active'."
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        "Sets this button to 'inactive'."
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = False

    def clicked(self, p):
        "Returns true if button active and p is inside"
        return self.active and \
               self.xmin <= p.getX() <= self.xmax and \
               self.ymin <= p.getY() <= self.ymax

    def getLabel(self):
        return self.label;

buttons = [[Button(win, Point(0, 0), 0,0, '0') for j in range(cols)] for i in range(rows)]

class Displays: 
    def __init__(self):
        self.myeqtTextString = ''
        self.myTextString = '0'

        self.myeqtTextString = str(self.myeqtTextString).rjust(200)
        self.eqtdisplayTextElement = Text(Point(0, 15), self.myeqtTextString)
        self.eqtdisplayTextElement.draw(win)

        self.myTextString = str(self.myTextString).rjust(200)
        self.displayTextElement = Text(Point(15, 75), self.myTextString)
        self.displayTextElement.draw(win)

    def redrawDisplays(self):
        self.eqtdisplayTextElement.undraw()
        self.eqtdisplayTextElement = Text(Point(0, 15), self.myeqtTextString)
        self.eqtdisplayTextElement.draw(win)

        self.displayTextElement.undraw()
        self.displayTextElement = Text(Point(15, 75), self.myTextString)
        self.displayTextElement.draw(win)

class Calculator:
    def __init__(self):
        self.group = 0
        self.xy = False
        self.xyval=0
        self.memory = 0
        self.cleardisplay = False
        self.displayString = '0'
        self.eqtdisplayString = ''

    
    def createCalculatorButtons(self):
        for i in range(rows):
            for j in range(cols):
                buttons[i][j] = Button(win, Point(j*80+40, i*80+140), 80,80, calcGrid[i][j])
                buttons[i][j].activate()

    def clickedButton(self, clicked):
        for i in range(rows):
            for j in range(cols):
                if buttons[i][j].clicked(clicked) == True:
                    return i, j
        return -1, -1

    def formatResult(self, theresult):
        resultString = str(theresult)
        formattedString = str(resultString).rjust(200)
        return formattedString

    def calculateresult(self, evalString):
        result = 0
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
        return str(result)

    def calculategroup(self, grp, dispstring, eqtdisp):
        if grp <= 1:
            i = eqtdisp.rfind('(')
            j = eqtdisp.find(')')
            newstring = eqtdisp[i+1:j]
            disp = self.calculateresult(newstring)
            if j != len(eqtdisp)-1:
                #more to the equation
                nexteqt = eqtdisp[j+1:] + dispstring
                newstring = str(disp) + nexteqt
                disp = self.calculateresult(newstring)     
        else:
            i = eqtdisp.rfind('(')
            j = eqtdisp.find(')')
            newstring = eqtdisp[i+1:j]
            disp = self.calculateresult(newstring)
        return disp, eqtdisp

    def memorybuttonpressed(self, newstring, memory, displayString):
        if newstring == "MC":
            memory = 0
            result = self.displayString
        elif newstring == "MR":
            result = memory
        elif newstring == "MS":
            memory = self.displayString
            result = self.displayString
        elif newstring == "M+":
            result = add2numbers(float(memory), float(self.displayString))
        elif newstring == "M-":
            result = subtract2numbers (float(memory), float(self.displayString))
        return memory, result

    def advancedbuttons(self, newstring, displayString):
        if newstring == "+/-":
            result = changesign(float(self.displayString))
        elif newstring == "%":
            result = percent(float(self.displayString))
        elif newstring == "\u221A":
            result = squareroot(float(self.displayString))
        elif newstring == "x\u00b2":
            result = square(float(self.displayString))
        elif newstring == "1/x":
            result = inverse(float(self.displayString))
        elif newstring == "sin":
            result = sin(float(self.displayString))
        elif newstring == "cos":
            result = cos(float(self.displayString))
        elif newstring == "tan":
            result = tan(float(self.displayString))
        elif newstring == "sin^-1":
            fdisplay = float(self.displayString)
            if fdisplay >= -1 and fdisplay <= 1:
                result = arcsin(float(fdisplay))
            else:
                result = "0"
        elif newstring == "cos^-1":
            fdisplay = float(self.displayString)
            if fdisplay >= -1 and fdisplay <= 1:
                result = arccos(float(fdisplay))
            else:
                result = "0"
        elif newstring == "tan^-1":
            result = arctan(float(self.displayString))
        elif newstring == "10^x":
            result = tenx(float(self.displayString))
        elif newstring == "log":
            result = log(float(self.displayString))
        elif newstring == "ln":
            result = ln(float(self.displayString))

        result= "%.4f" % round(float(result), 2)
        return result

    def calcrun(self):
        self.createCalculatorButtons()
        mydisplays = Displays()
        
        while 1==1:
            clicked = win.getMouse()
            row, col = self.clickedButton(clicked)

            buttons[row][col].deactivate()
            
            newstring = str(calcGrid[row][col])
            #check to make sure they didn't click on an empty square

            if newstring == '':
                continue
            if newstring == 'Quit':
                quit()
                                       
            if row == 0 : # Memory buttons
                self.memory, self.displayString = self.memorybuttonpressed(newstring, self.memory, self.displayString)
                        
            elif row == 1 or row == 2: #advanced calculator buttons that will return a result if not a group
                if self.group == 0:
                    self.displayString  = self.advancedbuttons(newstring, self.displayString)
                else:
                    if self.group == 2:
                        self.eqtdisplayString = '(' + newstring + self.eqtdisplayString[1:]
                    else:
                        self.eqtdisplayString = newstring + self.eqtdisplayString
                    self.displayString  = self.advancedbuttons(newstring, self.displayString)
                    
            elif newstring == "C":
                self.result = '0'
                self.displayString = '0'
                self.eqtdisplayString = ''
                self.group = 0
                self.xy = False
                self.xyval = 0

                         
            elif newstring == "CE":
                self.displayString = '0'
                self.result = '0'
                self.xy = False
                self.xyval = 0

                
            else: # primary calculator buttons
                if newstring.isdigit() == True: #number pressed
                    if self.displayString == '0':
                        self.displayString = newstring
                    elif self.cleardisplay == True:
                        self.displayString = newstring
                        self.cleardisplay = False
                    else:
                        self.displayString = self.displayString + newstring

                elif newstring == '(':
                    self.group = self.group + 1
                    self.eqtdisplayString  = self.eqtdisplayString + newstring
                            
                elif newstring == ')':
                    #check to make sure there was a '(' first
                    if self.group == 0:
                        continue
                    self.eqtdisplayString  = self.eqtdisplayString + self.displayString + newstring
                    #calculate
                    self.displayString, self.eqtdisplayString = self.calculategroup(self.group, self.displayString, self.eqtdisplayString)
                    self.cleardisplay = False

                elif newstring == "x^y":
                    self.xy = True
                    self.xyval = float(self.displayString)
                    self.displayString = '0'
                  
                        
                else: # something besides a number or group
                    if  newstring != "=" : #something besides =
                        if newstring == ".":
                            self.displayString = self.displayString + newstring
                        else:
                            self.cleardisplay = True
                            if self.eqtdisplayString == '':
                                self.eqtdisplayString = self.displayString + newstring
                            else:
                                if self.eqtdisplayString.find(')') > -1:
                                    self.eqtdisplayString  = self.eqtdisplayString + newstring        
                                else:    
                                    self.eqtdisplayString  = self.eqtdisplayString + self.displayString + newstring
                                
                                
                    else: #calculate
                        if self.xy == True:
                            self.result = xyfunc(self.xyval, float(self.displayString))
                            self.displayString = str(self.result)
                            self.xy = False
                            self.xyval = 0
                            self.eqtdisplayString = ""
                            self.cleardisplay = True
                   
                        else:
                            self.displayString = self.displayString.lstrip()
                            self.eqtdisplayString = self.eqtdisplayString.lstrip()
                            self.cleardisplay = True
                            if self.eqtdisplayString.find(')') > -1:
                                self.displayString, self.eqtdisplayString = self.calculategroup(self.group, self.displayString, self.eqtdisplayString)
                            else:
                                self.displayString = self.calculateresult(self.eqtdisplayString + self.displayString)
                            self.eqtdisplayString = ""
           
            mydisplays.myeqtTextString = self.formatResult(self.eqtdisplayString)       
            mydisplays.myTextString = self.formatResult(self.displayString)

            mydisplays.redrawDisplays()

                                
            for i in range(rows):
                for j in range(cols):
                    if not(i == row and j == col):
                        buttons[i][j].activate()


def main():
       
    myCalc = Calculator()
    myCalc.calcrun()
   
main()
