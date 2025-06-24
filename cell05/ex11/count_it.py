#!/usr/bin/env python3
import sys
args = sys.argv
if (len(args)-1) < 1:
    print("none")
else:
    print(f"parameters: {len(args)-1}")
    for arg in args[1:]:
        print(f"{arg}: {len(arg)}")