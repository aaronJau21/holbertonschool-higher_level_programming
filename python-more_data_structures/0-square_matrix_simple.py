#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_array = []
    for arr in matrix:
        new_array.append(list(map(lambda num: (round(num ** 2)), arr)))
    return (new_array)
