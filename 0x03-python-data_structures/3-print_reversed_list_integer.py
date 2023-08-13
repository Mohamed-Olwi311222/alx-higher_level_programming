#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    reverse = my_list.reverse()
    for item in reverse:
        print("{:d}".format(item))
