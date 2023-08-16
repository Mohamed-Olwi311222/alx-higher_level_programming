#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or not a_dictionary:
        return None

    best_value = 0
    best_key = None
    for key, value in a_dictionary.items():
        if best_value < value:
            best_value = value
            best_key = key
    return best_key
