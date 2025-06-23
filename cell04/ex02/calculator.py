#!/usr/bin/env python3
try:
    first_num = int(input("Give me the first number: "))
    second_num = int(input("Give me the second number: "))
    addition = first_num + second_num
    subtraction = first_num - second_num
    try:
        division = first_num // second_num
    except ZeroDivisionError:
        division = None
    multiplication = first_num * second_num
    print(f"{first_num} + {second_num} = {addition}")
    print(f"{first_num} - {second_num} = {subtraction}")
    if division == None:
        print("The denominator can't be zero!")
    else:
        print(f"{first_num} / {second_num} = {division}")
    print(f"{first_num} * {second_num} = {multiplication}")
except ValueError:
    print("Invalid! Please enter number only")