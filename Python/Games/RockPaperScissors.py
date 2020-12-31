# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 12:07:49 2020

@author: Nucte
"""

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

my_score = 0
computer_score = 0
images = [rock, paper, scissors]


print("Welcome in Rock Paper Scissors")
how_long = int(input("To what score would you like to play? "))

while my_score < how_long or computer_score < how_long:
    my_pick = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors " ))
    if my_pick >= 3 or my_pick < 0:
        print("Invalid number, you loose!")
        break
    else:
        print("Your choice: ")
        print(images[my_pick])
        
    computer_pick = random.randint(0,2)
    print("Computer choice: ")
    print(images[computer_pick])
    
    if my_score == (how_long-1):
        print("Congrats, you've won")
        print(f"Your score is {my_score} and computer score is {computer_score}")
        break
    elif computer_score == (how_long-1):
        print("Computer won!")
        print(f"Your score is {my_score} and computer score is {computer_score}")
        break
    
    if my_pick == computer_pick:
        print("It's draw!")
        print(f"Your score is {my_score} and computer score is {computer_score}")
    elif my_pick == 0 and computer_pick == 2:
        print("You win!")
        my_score += 1
        print(f"Your score is {my_score} and computer score is {computer_score}")
    elif my_pick == 1 and computer_pick == 0:
        print("You win!")
        my_score += 1
        print(f"Your score is {my_score} and computer score is {computer_score}")
    elif my_pick == 2 and computer_pick == 1:
        print("You win")
        my_score += 1
        print(f"Your score is {my_score} and computer score is {computer_score}")
    else:
        print("You loose!")
        computer_score += 1
        print(f"Your score is {my_score} and computer score is {computer_score}")
        
    
