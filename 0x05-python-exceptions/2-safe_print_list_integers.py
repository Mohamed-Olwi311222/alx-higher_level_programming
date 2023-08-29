#!/usr/bin/ptyhon3
def safe_print_list_integers(my_list=[], x=0):
    if my_list is None:
        return 0
    count = 0
    for i in range(x):
        try:
            value = int(my_list[i])
            print("{:d}".format(value), end="")
            count += 1
        except (ValueError, TypeError):
            pass
    print()
    return count
