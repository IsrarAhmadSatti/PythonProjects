#Number Guessing Game

##^Random Number Generation
##random.random() generates a random number between 0 and 1 (1 excluded)
##we multiply it by 10 expand range between 0 and 10 (10 excluded)
##and floor rounds it to lowest integer (0.5666 to 0 and 9.78 to 9)
##we add 1 to it to make the range from 1 to 10

import math
import random
from math import floor

def guessNumber(randomNumber):
    
    print("\tWELCOME TO NUMBER GUESSING GAME")
    print("Guess The number between 1 to 10")
    
    count = 0 #no of tries initialized from 0
    while True:

        try:
            guess = int(input("\nGuess the number I am thinking: "))
            #^ taking a guess from user

            if guess == randomNumber:
                count += 1
                print("Great. You guessed it right!!!")
                print("You got it after", count, " Tries")
                break

            else:
                count += 1 #counting no. of tries
                if guess > randomNumber:
                    print("Your number is on larger side: Try Again")

                else:
                    print("Your number is on smaller side: Try again")

        except ValueError: #validation Check
            print("Invalid Input!!!! Try AGain")

randomNumber = floor((random.random())* 10) + 1
guessNumber(randomNumber)

###Number Guessing Game
##import math
##import random
##from math import floor
##randomNumber = floor((random.random())* 10) + 1
##print("\tWELCOME TO NUMBER GUESSING GAME")
##print("Guess The number between 1 to 10")
##count=1
##while True:
##    guess = int(input("\nGuess the number I am thinking: "))
##    if guess == randomNumber:
##        print("Great you guessed it right!!!")
##        print("You got it in ",count," Tries")
##        break
##    else:
##        count+=1
##        print("\t!!!!!Wrong Guess!!!!!")
##    cont = input("Do you want to conitnue: yes or no: ")
##    if cont == "no" or cont == "NO" or cont == "No":
##        print("The number was: ",randomNumber)
##        print("\t----GAME OVER----")
##        break
##    elif cont == "yes" or cont == "YES" or cont =="Yes":
##        continue
##    else:
##        print("Wrong input: Try Again")
##        break          
