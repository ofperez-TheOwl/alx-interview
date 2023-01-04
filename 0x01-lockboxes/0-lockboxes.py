#!/usr/bin/python3
"""
0-lockboxes
Contains two functions to check if a list of boxes can be openned
TheOwl
"""

def canUnlockAll(boxes):
    """Check if any box hold the key of the next box
    """
    i, n = 0, len(boxes)
    if (n <= 1):
        return (True)

    while (i < n - 1):
        # no keys in the box
        if (len(boxes[i]) == 0):
            return (False)
        # check if any of the keys open the next box
        unlock = False
        for key in boxes[i]:
            if (key == i + 1):
                unlock = True
                break
        if (unlock == False):
            return (False)
        i = i + 1

    return (True)
