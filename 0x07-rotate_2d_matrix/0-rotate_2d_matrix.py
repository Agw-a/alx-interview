#!/usr/bin/python3
'''Rotates a 2D matrix
'''


def rotate_2d_matrix(matrix):
    """rotates a 2D matrix clockwise

    Args:
        2D matrix
    """
    if matrix is None:
        return
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return
    rows = len(matrix)
    columns = len(matrix[0])
    first, last = 0, rows-1

    while (first < last):
        matrix[first], matrix[last] = matrix[last], matrix[first]
        first += 1
        last -= 1
    for i in range(0, rows):
        for j in range(i + 1, columns):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


# if __name__ == "__main__":
#     matrix = [[1, 2, 3],
#               [4, 5, 6],
#               [7, 8, 9]]

#     rotate_2d_matrix(matrix)
#     for r in matrix:
#         print(r)
