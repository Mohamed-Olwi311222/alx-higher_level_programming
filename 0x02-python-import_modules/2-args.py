#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    print("{} arguments:".format(len(argv) - 1))
    for i, item in enumerate(argv[1:], start=1):
        print("{}: {}".format(i, argv[i]))
