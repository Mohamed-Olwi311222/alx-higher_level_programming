#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        big = 0
        for num in my_list:
            if big <= num:
                big = num
    return big
