# table.py
# This program prints a formatted table
import math

def main():
    temp = "{:4} {:4} {:5} {:4.1f}"
    for i in range (1,21):
        print(temp.format(i, i*10, i*100, math.sqrt(i*100)))


main()
