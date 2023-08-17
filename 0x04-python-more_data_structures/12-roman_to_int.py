#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    R = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
        }
    if roman_string[0] in R and len(roman_string) == 1:
        return R[roman_string[0]]

    sum = 0
    prev = R[roman_string[0]]
    for char in roman_string[1:]:
        curr = R[char]
        if prev >= curr:
            sum += prev
        else:
            sum -= prev
        prev = curr
    sum += curr
    return sum
