#!/usr/bin/env python3
try:
    num = int(input("Enter number: "))
    if num > 0:
        print("This number is positive")
    elif num < 0:
        print("This number is negative")
    elif num == 0:
        print("This number is both positive and negative")
except ValueError:
    print("Invalid! Please enter number only")