# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 12:28:19 2020

@author: Nucte
"""
from art import text2art
import random


print(text2art("Government\nDecisions\nSimulator"))

activities = {
1:"otwarte",
2:"zamknięte",
3:"W sumie częsc otwarta, czesc nie",
4:"Stan wojenny",
5:"Lewacki atak na państwo polskie",
6:"Wina opozycji",
7:"Przyznanie sie do bledu"
}


def decyzja_premiera():
    a = random.randint(1,6)
    return activities[a]

co = input("O czym premier ma zadecydować? ")
print(f"Oficjalne stanowisko rządu w sprawie {co}:",decyzja_premiera())