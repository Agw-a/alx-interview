#!/usr/bin/python3
from typing import List

"""Returns a list of integers representing a pascal's triangle
"""


def pascal_triangle(n: int) -> List[List[int]]:
    """function to print pascal's triangle

    Args:
        n (int): rows of the triangle

    Returns:
        List[List[int]]:List of list of integers representing the triangle
        if n <= 0 returns an empty list
    """
    res = [[1]]

    while n > 0:
        for i in range(n - 1):
            tmp = [0] + res[-1] + [0]
            row = []
            # define the next row
            for j in range(len(res[-1]) + 1):
                row.append(tmp[j] + tmp[j + 1])
            res.append(row)
        return res
