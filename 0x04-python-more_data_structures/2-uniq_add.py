#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    if my_list:
        for num in my_list:
            if num not in new_list:
                new_list.append(num)
    return sum(new_list)

