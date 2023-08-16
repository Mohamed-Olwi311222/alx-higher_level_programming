#!/usr/bin/python3
def number_keys(a_dictionary):
    count = 0
    if a_dictionary:
        keys = a_dictionary.keys()
        for count, _ in enumerate(keys):
            count += 1
    return count
