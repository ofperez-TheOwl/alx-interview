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
    # if number is prime the number of operations is itself
    if (i == n):
        return (i)

    # recursive instructions
    res = minOperations(n / i)
    if (res == 0):
        return (0)
    else:
        return (res + i)
