#!/usr/bin/python3
"""
 method that calculates the fewest number of operations needed to
 result in exactly n H characters in the file.
"""


def minOperations(n):
    """
    Calculates the fewest number of operations,
    required to result in exactly n 'H' characters.

    Args:
    n (int): The number of 'H' characters to reach.

    Returns:
    int: The minimum number of operations required
    to reach exactly n 'H' characters.
    """
    if n < 2:
        return 0

    ops = 0
    root = 2

    while root <= n:
        if n % root == 0:
            ops += root
            n = n / root
            root -= 1
        root += 1

    return ops
