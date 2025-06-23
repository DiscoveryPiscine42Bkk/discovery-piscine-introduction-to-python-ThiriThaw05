#!/usr/bin/env python3
try:
    num = int(input("Enter a number: \n"))
    for i in range (0,10):
        answer = i*num
        print(i,"x",num,"=",answer)
except ValueError:
    print("Invalid! Please enter a number only")