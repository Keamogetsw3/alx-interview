#!/usr/bin/python3
"""
N Queens program
"""
import sys


solutions = []
n = 0
pos = None


def get_input():
    """
    Retrieves the input value for N from the command line 
    arguments and validates it.

    Returns:
        int: The number of queens (N) specified by the user.

    Raises:
        SystemExit: If the input is invalid.
    """
    global n
    n = 0

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


def is_attacking(pos0, pos1):
    """
    Checks whether two queens are attacking each other on the chessboard.

    Arguments:
        pos0 (list): A list containing the row and column of the first queen.
        pos1 (list): A list containing the row and column of the second queen.

    Returns:
        bool: True if the queens are attacking each other, False otherwise.
    """
    if (pos0[0] == pos1[0]) or (pos0[1] == pos1[1]):
        return True
    return abs(pos0[0] - pos1[0]) == abs(pos0[1] - pos1[1])


def group_exists(group):
    """
    Checks if a solution group already exists in the list of solutions.

    Arguments:
        group: A list of queen positions representing a possible solution.

    Returns:
        bool: True if the group exists in the solutions list, False otherwise.
    """
    global solutions

    for stn in solutions:
        i = 0
        for stn_pos in stn:
            for grp_pos in group:
                if stn_pos[0] == grp_pos[0] and stn_pos[1] == grp_pos[1]:
                    i += 1
        if i == n:
            return True
    return False


def build_solution(row, group):
    """
    Recursively builds solutions to the N queens

    Arguments:
        row (int): The current row to place a queen on.
        group (list): The list of positions.
    """
    global solutions
    global n
    if row == n:
        tmp0 = group.copy()
        if not group_exists(tmp0):
            solutions.append(tmp0)
    else:
        for col in range(n):
            a = (row * n) + col
            matches = zip(list([pos[a]]) * len(group), group)
            used_positions = map(lambda x: is_attacking(x[0], x[1]), matches)
            group.append(pos[a].copy())
            if not any(used_positions):
                build_solution(row + 1, group)
            group.pop(len(group) - 1)


def get_solutions():
    """
    Generates all possible solutions to the N queens
    problem by recursively placing queens
    and ensuring they do not attack each other.
    """
    global pos, n
    pos = list(map(lambda x: [x // n, x % n], range(n ** 2)))
    a = 0
    group = []
    build_solution(a, group)


n = get_input()
get_solutions()

for solution in solutions:
    print(solution)
