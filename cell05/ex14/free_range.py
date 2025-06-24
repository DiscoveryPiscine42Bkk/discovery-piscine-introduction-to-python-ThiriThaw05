#!/usr/bin/env python3
import sys
args = sys.argv
if (len(args)-1) != 2:
    print("none")
else:
    arr = []
    first_arg = int(args[1])
    second_arg = int(args[2])
    for i in range (first_arg,second_arg+1,1):
        arr.append(i)
    print(arr)