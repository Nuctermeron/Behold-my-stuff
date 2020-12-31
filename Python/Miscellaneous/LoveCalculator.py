# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 10:28:42 2020

@author: Nucte
"""
print("Welcome in Love Calculator!")
name = input("What's your name? ")
name2 = input("What's his/her name? ")

name = name.lower()
name2 = name2.lower()

true_count = name.count('t') + name.count('r') + name.count('u') + name.count('e')
true_count2 = name2.count('t') + name2.count('r') + name2.count('u') + name2.count('e')
true_sum = true_count + true_count2
love_count = name.count('l') + name.count('o') + name.count('v') + name.count('e')
love_count2 = name2.count('l') + name2.count('o') + name2.count('v') + name2.count('e')
love_sum = love_count + love_count2

result = str(true_sum) + str(love_sum)
result = int(result)

if result < 10 or result > 90:
    print(f"Your score is {result}, you go together like coke and mentos")
elif 40 <= result <= 50:
    print(f"Your score is {result}, you are alright together")
else:
    print(f"Your score is {result}")
    
