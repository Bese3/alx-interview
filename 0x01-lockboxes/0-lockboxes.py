#!/usr/bin/python3
'''LockBoxes Challenge'''
from sys import setrecursionlimit


def canUnlockAll(boxes):
    '''determines if all the boxes can be opened or not
    Returns:
        True: all boxes can be opened
        False: not all boxes can be opened
    '''
    initial_index = 0
    keys = {0}
    checkboxes(boxes, initial_index, keys)
    zero_in = False
    for i in boxes:
        if 0 in i:
            zero_in = True

    if len(keys) > len(boxes) and zero_in:
        return False

    i = 0
    while i < len(keys):
        if i <= len(keys) - 2 and list(keys)[i + 1] != list(keys)[i] + 1:
            return False
        i += 1
    return True


def checkboxes(boxes, pos, keys):
    '''
    The function "checkboxes" recursively checks if all checkboxes
    can be selected based on the given positions and keys.
    '''
    setrecursionlimit(10000)
    if len(keys) == len(boxes):
        return True

    # if calls >= len(boxes):
    #     return keys

    if pos >= len(boxes):
        return

    for i in boxes[pos]:
        if i in keys:
            continue
        keys.add(i)
        # print(f"pos = {pos}, i = {i}, keys = {keys}")
        checkboxes(boxes, i, keys)
    return keys
