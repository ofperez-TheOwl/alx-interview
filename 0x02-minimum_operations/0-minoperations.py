#!/usr/bin/python3
"""
0-minoperations
"""


def minOperations(n: int) -> int:
    """Calculate the min of operations to obtain n"""
    # base cases
    if (n <= 1):
        return (0)
    if (n == 2):
        return (2)
    if (n == 3):
        return (3)

    # recursive instructions
    if (n % 2 == 0):
        res = minOperations(n / 2)
        if (res == 0):
            return (0)
        else:
            return (res + 2)
    else:
        if (n % 3 == 0):
            res = minOperations(n / 3)
            if (res == 0):
                return (0)
            else:
                return (res + 3)
        else:
            return (0)
