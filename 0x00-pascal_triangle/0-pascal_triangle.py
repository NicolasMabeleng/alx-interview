#!/usr/bin/python3
""" A module for working with Pascal triangle
"""


def pascal_triangle(n):
    """ returns pascal triangle
    """
    if n <= 0:
        return []

    pasTriangle = []

    for i in range(n):
        # first element
        my_List = [1]
        if i == 0:
            pasTriangle.append(my_List)
            continue

        k = i - 1
        for j in range(len(pasTriangle[k])):
            if j + 1 == len(pasTriangle[k]):
                # last element
                my_List.append(1)
                break
            # Add two previous values to get current next value
            nextVal = pasTriangle[k][j] + pasTriangle[k][j + 1]
            my_List.append(nextVal)
        pasTriangle.append(my_List)

    return pasTriangle
