#!/usr/bin/env python3
def greetings(name = "noble stranger"):
    if not isinstance(name,str):
        print("Error! It was not a name.")
    else:
        print(f"Hello, {name}.")
def main():
    greetings('Alexandra')
    greetings('Wil')
    greetings()
    greetings(42)
if __name__ == "__main__":
    main()