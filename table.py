# table.py
# This program prints a formatted table
import math

def main():
    temp = "{frst:4} {sec:4} {third:5} {fourth:4.1f}"
    for i in range (1,21):
        print(temp.format(frst=i, sec=i*10, third=i*100, fourth=math.sqrt(i*100)))


main()
