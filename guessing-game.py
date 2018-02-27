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
      if animalguess[0] == "q":
         return
      elif animalguess == answer :
         print("Congratualtions! That's correct!")
         guessedright = True
         question = input("Do you like this animal? Answer y or n: ")
         question = question.lower()
         if question[0] == "y":
            print("Cool! Me too!")
         elif question[0] == "n":
            print("Yeah I'm not a big fan of a", animalguess, "either")
         else :
            print("You were supposed to answer y or n... Goodbye")
      else:
         animalguess = input("Sorry that's incorrect. Try again: ")
         animalguess = animalguess.lower()
   return

main()

