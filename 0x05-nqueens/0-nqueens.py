#!/usr/bin/python3
""" N queens """


left_diag = set()
right_diag = set()
column = set()
result = []


def backtrack_nqueen(r, n):
    """
    `backtrack_nqueen` is a recursive backtracking
    algorithm to solve the N-Queens problem in Python.
    """
    # board = [0 for i in range(n) for j in range(n)]
    for c in range(n):
        if r + c in right_diag or r - c in left_diag or c in column:
            continue
        result.append([])
        left_diag.add(r - c)
        right_diag.add(r + c)
        column.add(c)
        result[-1].append(r)
        result[-1].append(c)
        if len(result) == n:
            print(result)
            # yield result
        backtrack_nqueen(r + 1, n)
        left_diag.remove(r - c)
        right_diag.remove(r + c)
        column.remove(c)
        result.pop(-1)
    # return solution


if __name__ == '__main__':
    from sys import argv
    try:
        n = int(argv[1])
    except IndexError:
        print('Usage: nqueens N')
        exit(1)
    except ValueError:
        print('N must be a number')
        exit(1)

    if n < 4:
        print('N must be at least 4')
        exit(1)

    backtrack_nqueen(0, n)
