from graphics import *

win = GraphWin('Calc', 300, 500)

def calcbutton(x, y, value):
    button = Rectangle(Point(x,y), Point (x + 100,y + 100))
    button.setFill('lightblue')
    button.draw(win)
    text = Text(Point(x + 50, y + 50), value)
    text.draw(win)
    return button

def inside (clicked, button):
    if clicked.getX() > button.p1.getX()and clicked.getX() < button.p2.getX():
            if clicked.getY() > button.p1.getY() and clicked.getY() < button.p2.getY():
                return True
    return False

def main():
    display = Rectangle(Point(0,0), Point(300, 100))
    display.setFill('lightgray')
    display.draw(win)
    button1 = calcbutton(0, 100, 5)
    button2 = calcbutton (100, 100, 6)
    button3 = calcbutton (200, 100, 7)
    displayString = ''
    text = Text (Point(0,0), '')
    text.draw(win)
    while 1 == 1:
        clicked = win.getMouse()
        if inside (clicked, button1):
                button1.setFill('navy')
                displayString = displayString + '5';
                text.undraw()
                text = Text(Point(300 - len(displayString) * 10, 50), displayString)
                text.draw(win)
                button2.setFill('lightblue')
                button3.setFill('lightblue')
        if inside (clicked, button2):
                displayString = displayString + '6';
                text.undraw()
                text = Text(Point(300 - len(displayString) * 10, 50), displayString)
                text.draw(win)
                button1.setFill('lightblue')
                button2.setFill('navy')
                button3.setFill('lightblue')
        if inside (clicked, button3):
                displayString = displayString + '7';
                text.undraw()
                text = Text(Point(300 - len(displayString) * 10, 50), displayString)
                text.draw(win)
                button1.setFill('lightblue')
                button2.setFill('lightblue')
                button3.setFill('navy')
        print(clicked.getX(), clicked.getY())
    
main()
