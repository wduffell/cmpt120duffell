# Introduction to Programming
# Lab Assignment #5
# Author: Willow Duffell
# Date: 2/26


#Define a variable to hold the name of an animal (this is the answer)

def main():
   guessedright = False
   answer = "pig"
   animalguess = input("I'm thinking of an animal... Try to guess it: ")
   animalguess = animalguess.lower()
   while guessedright == False :
      if animalguess == answer :
         print("Congratualtions! That's correct!")
         guessedright = True
      elif animalguess == "quit":
         return
      else:
         animalguess = input("Sorry that's incorrect. Try again: ")
         animalguess = animalguess.lower()
   return

main()

