# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 15:29:49 2020

@author: Nucte
"""
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



print("Welcome in Password generator!")
choice = int(input("Type 0 for simple and 1 for advanced password \n"))
number_letters = int(input("How many letters would you like in password?\n"))
number_symbols = int(input("How many symbols would you like in password?\n"))
number_numbers = int(input("How many numbers would you like in password?\n"))

#Simple password
if choice == 0:
    password = ""
    
    for char in range(1,number_letters + 1):
        random_letter = random.choice(letters)
        password += random_letter
        
    for char in range(1,number_symbols + 1):
        random_symbol = random.choice(symbols)
        password += random_symbol
        
    for char in range(1,number_numbers + 1):
        random_number = random.choice(numbers)
        password += random_number
    print(password)
    
#Advanced password
if choice == 1:
    passwordL = []

    for char in range(1, number_letters + 1):
      passwordL.append(random.choice(letters))
    
    for char in range(1, number_symbols + 1):
      passwordL += random.choice(symbols)
    
    for char in range(1, number_numbers + 1):
      passwordL += random.choice(numbers)
    
    random.shuffle(passwordL)

    password = ""
    for char in passwordL:
      password += char
    print(password)