#!/usr/bin/env python3
try:
    number = input("Give me a number: ")
    num = float(number)
    if num.is_integer():
        print("This number is a integer")
    else:
        print("This number is an decimal")
except ValueError:
    print("Invalid! Please enter number only.")
