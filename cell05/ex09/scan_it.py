#!/usr/bin/env python3
import sys
import re
if (len(sys.argv)-1) != 2:
    print("none")
else:
    first_parameter = sys.argv[1]
    second_parameter = sys.argv[2]
    matches = re.findall(first_parameter,second_parameter)
    if matches:
        print(len(matches))
    else:
        print("none")