#!/usr/bin/env python3
import sys
import re
args = sys.argv
if (len(args)-1) != 1:
    print("none")
else:
    character = "z"
    input_parameter = args[1]
    match = re.findall(character,input_parameter)
    if match:
        for chars in match:
            print(chars,end="")
        print()
    else:
        print("none")