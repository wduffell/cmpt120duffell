# Intro to Programming
# Author: Willow Duffell
# Date: 4/21/18
# Lab 9



class Product:
    def __init__(self, name, price, quantity): #constructor #self access attributes
        self.name = name
        self.price = price
        self.quantity = quantity #assign values
        
    def isinStock(self, count):
        if self.quantity >= count:
            return True
        else:
            return False

    def totalCost(self, count):
        return float(self.price) * int(count)

    def productRemove(self, count):
        self.quantity -= count
        return 

def printStock(myList):
    print()
    print("Available Products")
    print("------------------")
    num = len(myList)
    for i in range(0,len(myList)):
        if myList[i].quantity > 0:
            print(str(i)+")",myList[i].name, "$", myList[i].price)
    print()
    
    
def main():
    ProductList = [Product("Ultrasonic range finder", 2.50, 4),
                    Product("Servo motor", 14.99, 10),
                    Product("Servo controller", 44.95, 5),
                    Product("Microcontroller Board", 34.95, 7),
                    Product("Laser range finder", 149.99, 2),
                    Product("Lithium polymer battery", 8.99, 8)
                    ]
    
    cash = float(input("How much money do you have? $"))
    
    while cash > 0:

        printStock(ProductList)
               
        vals = input("Enter product ID and quantity you wish to buy: ").split(" ")
        if vals[0] == "quit": break
        
        prodId = int(vals[0])
        count = int(vals[1])

        instock = ProductList[prodId].isinStock(count)  
        if instock == True:
            
            if cash >= ProductList[prodId].totalCost(count):
                ProductList[prodId].productRemove(count)
                cash -= ProductList[prodId].price * count
                print("You purchased", count, ProductList[prodId].name + ".")
                print("You have $", "{0:.2f}".format(cash), "remaining.")
            else:
                print("Sorry, you cannot afford that product.")
            
        else:
            print("Sorry, we are sold out of", ProductList[prodId].name)
        

main()



