# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 15:00:55 2020

@author: Nucte
"""
import random

def dice():

    x = "Y"
    while x.upper() == "Y":
        number = random.randint(1,6)
    
        if number == 1:
            print("--------Y--")
            print("|         |")
            print("|    0    |")
            print("|         |")
            print("----------")
        if number == 2:
            print("----------")
            print("|         |")
            print("| 0     0 |")
            print("|         |")
            print("----------")
        if number == 3:
            print("----------")
            print("|         |")
            print("| 0  0  0 |")
            print("|         |")
            print("----------")
        if number == 4:
            print("----------")
            print("| 0     0 |")
            print("|         |")
            print("| 0     0 |")
            print("----------")
        if number == 5:
            print("----------")
            print("| 0     0 |")
            print("|    0    |")
            print("| 0     0 |")
            print("----------")
        if number == 6:
            print("----------")
            print("| 0     0 |")
            print("| 0     0 |")
            print("| 0     0 |")
            print("----------")
        x = input("Another throw? Y/N ")


dice()