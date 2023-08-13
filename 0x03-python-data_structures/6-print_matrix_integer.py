#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in matrix:
            for colm in row:
                print("{:d}".format(colm), end=' ' if colm != row[-1] else '')
            print()
