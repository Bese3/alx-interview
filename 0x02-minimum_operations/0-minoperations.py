#!/usr/bin/python3
'''this module computes the minimum operation problem'''


def minOperations(n):
    """
    The function `minOperations` calculates the minimum number of
    operations required to reduce a given number `n` to 1.
    """
    if n <= 1:
        return 0

    for i in range(2, n + 1):
        if n % i == 0:
            return i + minOperations(int(n / i))
