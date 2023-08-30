#!/usr/bin/python3
def uppercase(str):
    for current in str:
        if "a" <= current <= "z":
            current = chr(ord(current) - 32)
        print("{:s}".format(current), end="")
    print()
