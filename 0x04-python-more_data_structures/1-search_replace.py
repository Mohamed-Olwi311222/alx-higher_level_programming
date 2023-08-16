#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    if my_list:
        index = my_list.index(search)
        new_list.extend(my_list)
        new_list.pop(index)
        new_list.insert(index, replace)
    return new_list
