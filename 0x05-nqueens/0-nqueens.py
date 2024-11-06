#!/usr/bin/python3
""" 
The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard.
Write a program that solves the N queens problem.
"""
import sys


def print_solution(board):
    """Prints a solution in the required format"""
    solution = []
    for i in range(len(board)):
        solution.append([i, board[i]])
    print(solution)

def is_safe(board, row, col):
    """Checks if it's safe to place a queen at the board[row][col] position"""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(N):
    """Uses backtracking to solve the N queens problem and prints each solution"""
    def backtrack(row):
        if row == N:
            print_solution(board)
        else:
            for col in range(N):
                if is_safe(board, row, col):
                    board[row] = col
                    backtrack(row + 1)

    board = [-1] * N
    backtrack(0)
