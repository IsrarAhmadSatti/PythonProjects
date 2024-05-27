import random
from random import choices
print("ROCK, PAPER & SCISSOR")
my_wins = 0
com_wins = 0
options = ["ROCK", "PAPER", "SCISSOR"]

def user_move():
    inp = input("\nSelect the choice\n Rock, Paper,Scissor, Exit: ")
    return inp

def comp_move():
    choice = random.choices(options)
    return choice

while (True):
    usr_cho = input("\nSelect the choice\n 0:Rock, 1:Paper, 2:Scissor, 3:Exit: ")
    usr_cho = usr_cho.upper()
    print(usr_cho)
    rand_num = random.randint(0,2)
    com_choice = options[rand_num]
    
        
    if com_choice == "Rock" and usr_cho == "Paper" or usr_cho == "1":
        print("You WON!!!")
        print("Computer Chose ",com_choice)
        my_wins += 1

    elif com_choice == "Paper" and usr_cho == "Scissor" or usr_cho == "2":
        print("You WON!!!")
        print("Computer Chose ",com_choice)
        my_wins += 1

    elif com_choice == "Scissor" and usr_cho == "Rock" or usr_cho == "0":
        print("You WON!!!")
        print("Computer Chose ",com_choice)
        my_wins += 1
    elif com_choice == usr_cho:
        print("Try Again")
        print("Computer Chose ",com_choice)
        
    elif usr_cho == "Exit" or usr_cho == "exit" or usr_cho == "3":
        break
    else:
        print("You LOSE!!!")
        print("Computer Chose ",com_choice)
        com_wins += 1

    

print("\nYou won ",my_wins,"times")
print("Computer won",com_wins,"times")


