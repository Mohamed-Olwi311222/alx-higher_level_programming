#!/usr/bin/python3
for current in range(97, 123):
    if current == 113 or current == 101:
        continue
    print("{:s}".format(chr(current)), end="")
