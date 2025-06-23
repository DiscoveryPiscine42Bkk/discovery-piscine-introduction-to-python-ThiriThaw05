#!/usr/bin/env python3
text = input("")
swapped = ""
for char in text:
    if char.isupper():
        swapped += char.lower()
    elif char.islower():
        swapped += char.upper()
    else:
        swapped += char
print(swapped)
