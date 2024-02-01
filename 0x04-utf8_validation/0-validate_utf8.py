#!/usr/bin/python3
"""
utf-8 validation module
"""


def decimalToBinary(n):
    '''Converts an integer decimal to its binary representation.'''
    return bin(n).replace("0b", "")


def validUTF8(data):
    '''Returns True if data is a valid UTF-8 encoding, else return False
    data is a list of integers, each integer representing a byte'''

    i = 0
    while i < len(data):
        if len(decimalToBinary(data[i])) < 8:
            i += 1
            continue

        elif decimalToBinary(data[i])[0:3] == '110' and i + 1 < len(data):
            secondChar = decimalToBinary(data[i + 1])

            if len(secondChar) < 8:
                return False
            elif secondChar[0:2] == '10':
                i += 2
                continue

        elif decimalToBinary(data[i])[0:4] == '1110' and i + 2 < len(data):
            secondChar = decimalToBinary(data[i + 1])
            thirdChar = decimalToBinary(data[i + 2])
            if len(secondChar) < 8 or len(thirdChar) < 8:
                return False
            elif secondChar[0:2] == '10' and thirdChar[0:2] == '10':
                i += 3
                continue

        elif decimalToBinary(data[i])[0:5] == '11110' and i + 3 < len(data):
            secondChar = decimalToBinary(data[i + 1])
            thirdChar = decimalToBinary(data[i + 2])
            fourthChar = decimalToBinary(data[i + 3])
            if (len(secondChar) < 8 or len(thirdChar) < 8 or
                    len(fourthChar) < 8):
                return False
            elif (secondChar[0:2] == '10' and thirdChar[0:2] == '10' and
                  fourthChar[0:2] == '10'):
                i += 4
                continue
        else:
            return False

    return True
