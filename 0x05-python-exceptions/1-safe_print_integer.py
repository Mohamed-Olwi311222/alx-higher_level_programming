#!/usr/bin/pyhon3
def safe_print_integer(value):
    if value is None:
        return False
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        return False