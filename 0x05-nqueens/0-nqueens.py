#!/usr/bin/python3
import sys
''' N- Queens algorithm
'''


# validate input
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)

if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)


board_size = int(sys.argv[1])


def getNqueens(n, i=0, a=[], b=[], c=[]):
    """ validate queen positions on the board """
    if i < n:
        for j in range(n):
            if j not in a and i + j not in b and i - j not in c:
                yield from getNqueens(n, i + 1, a + [j], b + [i + j], c + [i - j])
    else:
        yield a


def solve(n):
    """ print placements on the board """
    k = []
    i = 0
    for solution in getNqueens(n, 0):
        for s in solution:
            k.append([i, s])
            i += 1
        print(k)
        k = []
        i = 0


solve(board_size)