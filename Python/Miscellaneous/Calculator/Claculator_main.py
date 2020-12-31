# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 11:52:16 2020

@author: Nucte
"""

from art import text2art

print(text2art("Calculator"))
#Add
def add(n1,n2):
    return n1 + n2

#Substract
def substract(n1,n2):
    return n1-n2

#Divide
def divide(n1,n2):
    return n1/n2

#Multiply
def multiply(n1,n2):
    return n1*n2

operations = {
 "+": add,
 "-": substract,
 "*": multiply,
 "/": divide
}




num1 = int(input("What's the first number?: "))
num2 = int(input("What's the second number?: "))

for symbol in operations:
    print(symbol)
operation_symbol = input("Pick an operation from the line above: ")


calculation_function = operations[operation_symbol]
result = calculation_function(num1,num2)
print(f"{num1} {operation_symbol} {num2} = {result}")

should_stop = ""
while should_stop != "n":
 should_stop = input(f"Type 'y' to continue calculating with {result}, or type 'n' to exit: ")
 operation_symbol = input("Pick an operation from the line above: ")
 num = int(input("What's your next number? "))
 calculation_function = operations[operation_symbol]
 result_loop = calculation_function(result,num)
 print(f"{result} {operation_symbol} {num} = {result_loop}")
 result = result_loop
 
 
 
