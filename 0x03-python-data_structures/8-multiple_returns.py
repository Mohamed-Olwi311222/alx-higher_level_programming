#!/usr/bin/python3
def multiple_returns(sentence):
    first = None
    length = len(sentence)
    t = ()
    if length == 0:
        t = (length, first)
    else:
        first = sentence[0]
        t = (length, first)
    return t
