#!/usr/bin/env python3
import sys
def add_one(num):
    num+=1
    print(f"Inside the function: {num}")

def main():
    num = 20
    print(f"Before calling the function: {num}")
    add_one(num)
    print(f"After calling the function: {num}")
if __name__ == "__main__":
    main()

#What do you observe?
#Integer is immutable in Python and also parameter num in add_one function is a local copy so modifying it doesn't affect the original number in main program
