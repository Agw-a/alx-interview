#!/usr/bin/python3
import sys
''' N- Queens algorithm
'''


def isSafe(board, row, i):
    '''checks if it's okay to insert a queen at colunm i in a row on the board
    '''
    for q in range(row):
        if (board[q] == i or
                board[q] + row - q == i or
                board[q] + q - row == i):
            return False
    return True


def Fill_Rows(board, row):
    '''Fills rows in board with right index
    '''
    for q in range(len(board)):
        if isSafe(board, row, q):
            board[row] = q
            if row < len(board) - 1:
                Fill_Rows(board, row + 1)
            else:
                print([[q, board[q]] for i in range(len(board))])


# validate input
n = int(sys.argv[1])
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)

if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)

board = [-1 for i in range(n)]
Fill_Rows(board, 0)
