#!/usr/bin/env python3
import sys
if (len(sys.argv)-1) != 1:
    print("none")
else:
    user = input("What was the parameter? ")
    if sys.argv[1] == user:
        print("Good job!")
    else:
        print("Nope,sorry...")