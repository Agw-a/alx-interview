#!/usr/bin/python3

"""
This module defines the function `minOpertions`
"""


def minOperations(n):
    '''Calculates minimum c&p tasks on a text file
    '''
    if n < 1 or type(n) != int:
        return 0
    ops = 0
    while n >= 2:
        lf = 2
        while lf < n + 1:
            if n % lf == 0:
                ops += lf
                n /= lf
                break
            lf += 1
    return ops
