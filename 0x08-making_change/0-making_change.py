#!/usr/bin/python3
"""
makeChange
Determine the minimal number of coins needed to meet
a given amount and a certains set of coins
"""


def makeChange(coins, total):
    # coins : a list of available coins
    # total : amount to meet

    if (total <= 0):
        return (0)
    n = 0

    # sort the coins
    coins.sort(reverse=True)

    for coin in coins:
        n = n + total // coin
        rest = total % coin
        if (rest == 0):
            return (n)
        total = rest

    return (-1)
