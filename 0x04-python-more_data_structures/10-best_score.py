#!/usr/bin/python3
def best_score(a_dictionary):
    for key, value in a_dictionary.items():
        if best < value:
            best = value
    if best == 0:
        return None
    return best
