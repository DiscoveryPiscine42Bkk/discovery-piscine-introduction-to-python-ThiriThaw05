#!/usr/bin/env python3
import sys
if (len(sys.argv)-1) < 1:
    print("none")
else:
    if (sys.argv[1].islower()):
        print(sys.argv[1].upper())
    else:
        print("Please pass arguments in lower case!")