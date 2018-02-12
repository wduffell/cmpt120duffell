# Introduction to Programming
# Author: Willow Duffell
# Date: 2/5/18

def fibonacci (n):
    if n == 1 or n == 2:
        return 1
    return fibonacci (n-1) + fibonacci (n-2)

# JA: You also need this
def main():
    n = int(input("Enter a term number: "))
    print("The fibonnaci number is ",fibonacci(n))

main()

    
    
