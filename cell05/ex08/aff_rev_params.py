#!/usr/bin/env python3
import sys
if (len(sys.argv)-1) < 2:
    print("none")
else:
    for args in reversed(sys.argv):
        print(args)