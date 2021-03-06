# Introduction to Programming
# Author: Willow Duffell
# Date: 2/5/18

import math

def main():
    n = int (input ("Enter the number of terms to use:"))
    sign = 1
    pi = 0
    for i in range (1, n * 2 + 1, 2):
        term = 4/i * sign
        pi = pi + term
        sign = sign * -1
    print ("The approximated value of pi is:", pi)
    print ("The error of the estimate is", math.fabs (pi - math.pi))

main()




        
