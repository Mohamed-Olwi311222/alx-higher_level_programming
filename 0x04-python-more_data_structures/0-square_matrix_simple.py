#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    if matrix:

        for row in matrix:
            squared_row = []
            for num in row:
                squared_row.append(num ** 2)

            new_matrix.append(squared_row)

    return new_matrix
