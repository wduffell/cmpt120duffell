#Intro to Programming
#Author: Willow DUffell
#Date: 2/23/

#Calculator functions

import math 

def add2numbers(x,y):
    return x + y
def subtract2numbers(x,y):
    return x - y
def multiply2numbers(x,y):
    return x * y
def divide2numbers(x,y):
    return x / y
def changesign(x):
    return x * -1
def percent(x):
    return x / 100
def squareroot(x):
    return x ** .5
def square(x):
    return x ** 2
def inverse(x):
    return 1 / x
def xyfunc(x,y):
    return x ** y
def sin(x):
    return math.sin(math.radians(x))
def cos(x):
    return math.cos(math.radians(x))
def tan(x):
    return math.tan(math.radians(x))
def tenx(x):
    return 10 ** x
def log(x):
    return math.log10(x)
def arcsin(x):
    x = math.asin(x)
    return math.degrees(x)
def arccos(x):
    x = math.acos(x)
    return math.degrees(x)
def arctan(x):
    x = math.atan(x)
    return math.degrees(x)
def ln(x):
    return math.log(x)
