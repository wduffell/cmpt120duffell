# Change.py

def main():
    print("Change Counter")
    print()
    print("Please enter the count of each coin type.")
    quarters = int(input("Quarters: "))
    dimes = int(input("Dimes: "))
    nickels = int(input("Nickels: "))
    pennies = int(input("Pennies: "))
    total = .25 * quarters + .10 * dimes + .05 * nickels + .01 * pennies
    fee = total * .03
    print()
    str = "The total value of your change is ${0:0.2f}. Your fee is ${1:0.2f}"
    print(str.format(total, fee))

main()
