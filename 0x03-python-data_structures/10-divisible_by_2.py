#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    isdiv = []
    if my_list:
        for num in my_list:
            if num % 2 == 0:
                isdiv.append(True)
            else:
                isdiv.append(False)
    return isdiv
