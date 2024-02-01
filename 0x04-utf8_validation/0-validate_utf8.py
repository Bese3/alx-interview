#!/usr/bin/python3
"""
utf-8 validation module
"""


def validUTF8(data):
    """
    The function checks if the given data is a
    valid UTF-8 encoded string.
    """
    try:
        utf8 = bytes(data)
    except ValueError:
        return False
    return True
