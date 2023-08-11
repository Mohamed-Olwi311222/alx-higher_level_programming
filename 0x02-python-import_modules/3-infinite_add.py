#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    args = argv[1:]
    sum = 0
    for arg in args:
        sum += int(arg)
    print('{}'.format(sum))