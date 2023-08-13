#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        sum = 0
        for num in my_list:
            sum += num
    return sum
