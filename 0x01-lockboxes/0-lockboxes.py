#!/usr/bin/python3
"""
method that determines if all the boxes can be opened
"""


def canUnlockAll(boxes):
    """
    Check if all boxes can be opened

    Args:
    boxes: is a list of lists

    Return: True if all boxes can be opened, else return False
    """
    n = len(boxes)
    seen_boxes = set([0])
    unseen_boxes = set(boxes[0]).difference(set([0]))
    while len(unseen_boxes) > 0:
        boxIdx = unseen_boxes.pop()
        if not boxIdx or boxIdx >= n or boxIdx < 0:
            continue
        if boxIdx not in seen_boxes:
            unseen_boxes = unseen_boxes.union(boxes[boxIdx])
            seen_boxes.add(boxIdx)
    return n == len(seen_boxes)
