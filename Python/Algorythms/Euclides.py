# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 17:01:53 2020

@author: Nucte
"""

def Euclides_a(a, b):
    while a%b != 0:
        modulo = a%b
        a = b
        b = modulo
    print(modulo)
    

Euclides_a(32, 12)
    