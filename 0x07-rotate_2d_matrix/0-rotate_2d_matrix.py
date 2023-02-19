#!/usr/bin/python3
'''Rotates a 2D matrix
'''


def rotate_2d_matrix(matrix):
    """rotates a 2D matrix clockwise

    Args:
        2D matrix
    """
    for i in range(len(matrix)):
        for n in range(i):
            temp = matrix[i][n]
            matrix[i][n] = matrix[n][i]
            matrix[n][i] = temp

    for i in range(len(matrix)):
        for j in range(len(matrix) // 2):
            temp = matrix[i][j]
            matrix[i][len(matrix) - j - 1] = temp
