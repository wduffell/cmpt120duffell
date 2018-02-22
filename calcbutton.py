from graphics import *

win = GraphWin('Calc', 320, 500)

# Create the text for the display area

displayTextElement = Text(Point(0, 50), "")

calcGrid = [
    [7, 8, 9, '+'],
    [4, 5, 6, '-'],
    [1, 2, 3, '*'],
    ['', 0, '+/-', '/'],
    ['', '', '', '=']
]
buttons = [['','','', '',''], ['', '', '', ''], ['', '', '', '', ''], ['', '', '', ''],['', '', '', '']]

def calcButton(x, y, value):
    button = Rectangle(Point(x,y), Point (x + 80, y + 80))
    button.setFill('lightblue')
    button.draw(win)
    text = Text(Point(x + 40, y + 40), value)
    text.draw(win)
    return button

def inside (clicked, button):
    if clicked.getX() > button.p1.getX()and clicked.getX() < button.p2.getX():
            if clicked.getY() > button.p1.getY() and clicked.getY() < button.p2.getY():
                return True
    return False

def clickedButton(clicked):
    for i in range(5):
        for j in range(4):
            if clicked.getX() > buttons[i][j].p1.getX()and clicked.getX() < buttons[i][j].p2.getX():
                if clicked.getY() > buttons[i][j].p1.getY() and clicked.getY() < buttons[i][j].p2.getY():
                    return i, j
    return -1, -1

def createCalculatorButtons():
    for i in range(5):
        for j in range (4):
            buttons[i][j] = calcButton(j * 80, i * 80 + 100, calcGrid[i][j])

def main2():
    display = Rectangle(Point(0,0), Point(300, 100))
    display.setFill('lightgray')
    display.draw(win)
    button5 = calcbutton(0, 100, 5)
    button6 = calcbutton (100, 100, 6)
    button7 = calcbutton (200, 100, 7)
    displayString = ''
    text = Text (Point(0,0), '')
    text.draw(win)
    while 1 == 1:
        clicked = win.getMouse()
        if inside (clicked, button5):
                button5.setFill('navy')
                displayString = displayString + '5';
                text.undraw()
                text = Text(Point(300 - len(displayString) * 10, 50), displayString)
                text.draw(win)
                button6.setFill('lightblue')
                button7.setFill('lightblue')
        if inside (clicked, button6):
                displayString = displayString + '6';
                text.undraw()
                text = Text(Point(300 - len(displayString) * 10, 50), displayString)
                text.draw(win)
                button5.setFill('lightblue')
                button6.setFill('navy')
                button7.setFill('lightblue')
        if inside (clicked, button7):
                displayString = displayString + '7';
                text.undraw()
                text = Text(Point(300 - len(displayString) * 10, 50), displayString)
                text.draw(win)
                button5.setFill('lightblue')
                button6.setFill('lightblue')
                button7.setFill('navy')
        print(clicked.getX(), clicked.getY())




def main():
    createCalculatorButtons()
    displayString = ''
    displayTextElement = Text(Point(0, 50), "")
    displayTextElement.draw(win)
    while 1 == 1:
        clicked = win.getMouse()
        print (clicked.getX(), clicked.getY())
        row, col = clickedButton(clicked)
        if row > 0 :
            buttons[row][col].setFill('lightgreen')
            displayString = displayString + str(calcGrid[row][col]).rjust(150);
            displayTextElement = Text(Point(0, 50), displayString)
            displayTextElement.draw(win)
            print (calcGrid[row][col])
        for i in range(5):
            for j in range(4):
                if not(i == row and j == col):
                    buttons[i][j].setFill('lightblue')




main()
