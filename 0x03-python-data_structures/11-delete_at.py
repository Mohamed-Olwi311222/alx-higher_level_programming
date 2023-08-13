#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if my_list and idx < len(my_list):
        new_list = []
        for i in range(len(my_list)):
            if i != idx:
                new_list.append(my_list[i])
        my_list.clear()
        my_list.extend(new_list)
        return new_list
    else:
        return my_list
