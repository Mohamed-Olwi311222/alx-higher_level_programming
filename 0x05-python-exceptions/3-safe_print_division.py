#!/usr/bin/ptyhon3
def safe_print_division(a, b):
    if a is None or b is None:
        return
    try:
        div = a / b
        print("{:d} / {:d} = {:d}".format(a, b, div))
    except ZeroDivisionError:
        
