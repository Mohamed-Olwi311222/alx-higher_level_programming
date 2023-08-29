#!/usr/bin/pyhon3
def safe_print_division(a, b):
    if a is None or b is None:
        return
    try:
        div = a / b
    except ZeroDivisionError:
        div = None
    finally:
        print("Inside result: {}".format(div))
    return div
