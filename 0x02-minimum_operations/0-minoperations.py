#!/usr/bin/python3
"""
0-minoperations
"""


def minOperations(n):
    """Calculate the min of operations to obtain n"""
    # base cases
    if (n <= 1):
        return (0)
    i = 2
    while (i < n):
        if (n % i == 0):
            break
        i = i + 1
    if (i == n):
        return (i)

    # recursive instructions
    if (n % 2 == 0):
        res = minOperations(n / 2)
        if (res == 0):
            return (0)
        else:
            return (res + 2)
    elif (n % 3 == 0):
        res = minOperations(n / 3)
        if (res == 0):
            return (0)
        else:
            return (res + 3)
