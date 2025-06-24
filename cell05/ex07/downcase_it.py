#!/usr/bin/env python3
import sys
if (len(sys.argv)-1) < 1:
    print("none")
else:
    if (sys.argv[1].isupper()):
        print(sys.argv[1].lower())
    else:
        print("Please pass arguments in upper case!")