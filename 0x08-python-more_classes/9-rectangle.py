#!/usr/bin/python3
import sys


def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]"""
    # Check the row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check the upper diagonal on the left side
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check the lower diagonal on the left side
    i, j = row, col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve_nqueens(board, col):
    """Recursive function to solve the N Queens problem"""
    # If all queens are placed, print the solution
    if col >= N:
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append([i, j])
        print(solution)
        return True

    # Consider this column and try placing the queen in all rows
    for row in range(N):
        if is_safe(board, row, col):
            # Place the queen in the current position
            board[row][col] = 1

            # Recur to place the rest of the queens
            solve_nqueens(board, col + 1)

            # Backtrack and remove the queen from the current position
            board[row][col] = 0


# Check the number of command-line arguments
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

# Get the value of N from the command-line argument
try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

# Check if N is at least 4
if N < 4:
    print("N must be at least 4")
    sys.exit(1)

# Create an empty chessboard
chessboard = [[0 for _ in range(N)] for _ in range(N)]

# Solve the N Queens problem
solve_nqueens(chessboard, 0)
