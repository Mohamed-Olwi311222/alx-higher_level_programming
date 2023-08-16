#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    if my_list:
        new_list.extend(my_list)
        for i, _ in enumerate(new_list):
            if new_list[i] == search:
                new_list.pop(i)
                new_list.insert(i, replace)
                
    return new_list
