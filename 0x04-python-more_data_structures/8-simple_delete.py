#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key and a_dictionary:
        a_dictionary.pop(key)
    return a_dictionary
