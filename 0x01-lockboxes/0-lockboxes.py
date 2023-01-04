#!/usr/bin/python3
"""
0-lockboxes
Contains two functions to check if a list of boxes can be openned
TheOwl
"""


def canUnlockAll(boxes):
    """Check if any box hold the key of the next box
    """
    n = len(boxes)
    if (n == 0):
        return (False)
    if (n == 1):
        return (True)

    unlocked_boxes = [0]
    locked_boxes = [x for x in range(1, n)]
    while (len(locked_boxes) != 0):
        unlocked = len(unlocked_boxes)
        for i in unlocked_boxes:
            # check the boxes that can be open by the keys in this box
            for key in boxes[i]:
                if (key < n):
                    if (key not in unlocked_boxes):
                        unlocked_boxes.append(key)
                    if (key in locked_boxes):
                        locked_boxes.remove(key)
        if (unlocked == len(unlocked_boxes)):
            return (False)

    return (True)
