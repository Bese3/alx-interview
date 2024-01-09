#!/usr/bin/python3
'''
Module 0-pascal_triangle
Contains function pascal_triangle(n)
'''


def pascal_triangle(n):
    '''
    Pascal's triangle solver
    Args:
      n (int): The number of rows of the triangle
    Returns:
      List of list of numbers, each list representing a
    '''
    if n <= 0:
        return []
    my_list, temp, r = [], [], 0
    for i in range(n):
        while r <= i:
            temp.append(int(combination(i, r)))
            r += 1
        my_list.append(temp)
        temp = []
        r = 0
    return my_list


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def combination(n, r):
    """
    computes the combination of two numbers
    """
    num = factorial(n)
    den = factorial(n - r) * factorial(r)
    return num / den
