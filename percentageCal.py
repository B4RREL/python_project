#!/bin/python3
import time

def show_progress_bar(duration=10, steps=50):
    for i in range(steps):
        time.sleep(duration / steps)
        print(f"Loading: [{'#' * (i + 1)}{'.' * (steps - i - 1)}] {int((i + 1) / steps * 100)}%", end='\r')
    print()  # Move to the next line after completion

convert = input("Convert to (percentage or number) [P/N]:")

def calculatePercentage(por,total):
    result = round((por / total) * 100, 1)
    return result

def calculateNumber(por,total):
    result = round((por / 100) * total, 1)
    return result

if convert == "P":
    
    try:
        part = float(input("Please put part of the total(50 of 100,part is 50):"))
        total = float(input("Please put total o(50 of 100,total is 100):"))# comment: 
    except:
        print("Your inputs are not valid.")
    else:  
        show_progress_bar() 
        print(f"{part} of {total} is {calculatePercentage(part, total)}%")
        
        
elif convert == "N":
    try:
        part = float(input("Please put percentage of the 100%(50 of 100%,percentage is 50):"))
        total = float(input("Please put total o(50 of 100,total is 100):"))
    except:
        print("Your inputs are not valid.")
    else:
        show_progress_bar()
        print(f"{part}%  of {total} is {calculateNumber(part, total)}")
else:
    print(f"Please select which one you want to convert!")