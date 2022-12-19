#!/usr/bin/python3
"""
0-pascal_triangle
Contains a function to generate a Pascal triangle
TheOwl
"""


def pascal_triangle(n):
    """Compute each element of nth line of a Pascal's triangle
    """
    # base cases
    if (n <= 0):
        return ([])
    elif (n == 1):
        return ([[1]])
    elif (n == 2):
        return ([[1], [1, 1]])

    # recursive instructions
    triangle = pascal_triangle(n - 1)
    tmp_list = [1]
    for i in range(1, n - 1):
        element = triangle[n - 2][i - 1] + triangle[n - 2][i]
        tmp_list.append(element)
    tmp_list.append(1)
    triangle.append(tmp_list)
    return (triangle)
