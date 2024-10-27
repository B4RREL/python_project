#!/bin/python3

import sys
import socket
import math

import time
import sys

toolbar_width = 40

# setup toolbar
sys.stdout.write("[%s]" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['

for i in range(toolbar_width):
    time.sleep(0.1) # do real work here
    # update the bar
    sys.stdout.write("-")
    sys.stdout.flush()

sys.stdout.write("]\n") # this ends the progress bar
# name = "Bro"
# int = 34
# fla = 8.5
# is_student = True

# def calculate(num1, num2, operator):
#     if operator == "+":
#         result = num1 + num2
#         print(result)
#     elif operator == "-":
#         result = num1 - num2
#         print(result)
#     elif operator == "*":
#         result = num1 * num2
#         print(result)
#     elif operator == "/":
#         result = num1 / num2
#         print(result)
#     else:
#         print(f"{operator} is not a valid operator.")


# operator = input("Please select the operator(+ - * /):")
# num1 = float(input("Please type your first number:"))
# num2 = float(input("Please type your second number:"))

# calculate(num1, num2, operator)



