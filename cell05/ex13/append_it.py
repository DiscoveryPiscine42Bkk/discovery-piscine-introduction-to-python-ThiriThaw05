#!/usr/bin/env python3
import sys
import re
args = sys.argv[1:]
if (len(args)-1) < 1:
    print("none")
else:
    for arg in args:
        if arg[-3:] == "ism":
            continue
        else:
            print(arg+"ism")