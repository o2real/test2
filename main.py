from art import logo
print(logo)

import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(guess, computer_choice) :
  if guess > computer_choice:
    print("Too high.")
  elif guess < computer_choice :
    print("Too low.")
  else:
    print(f"You got it ! The answer was{computer_choice}.")

def set_diff():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy" :
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS 


#Choosing a random number 1 ~ 100
print("Welcom to guess game!")
print("I'm thinking of a number between 1 and 100.")
computer_choice = random.randint(1,100)



guess = int(input("Choose Your number! : "))
turns = set_diff()
print(f"You have {turns} attempts remaining to guess the number.")

gogo = True

while gogo == True :

  if computer_choice > guess :
    print("LOW")
    gogo = True
  elif computer_choice < guess :
    print("High")
    gogo = True
  elif computer_choice == guess :
    print("You Win!")
    gogo = False
