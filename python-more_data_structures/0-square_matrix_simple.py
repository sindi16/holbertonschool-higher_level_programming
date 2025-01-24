#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_list = []
        for el in row:
            new_list.append(el ** 2)
        new_matrix.append(new_list)
    return new_matrix
    