#!/usr/bin/python3
"""
In a text file, there is a single character H.
Your text editor can execute only two operations in this file: Copy All and Paste.
Given a number n, write a method that calculates the fewest
number of operations needed to result in exactly n H characters in the file.
"""
def minOperations(n):
    """
    Returns an integer
    If n is impossible to achieve, return 0
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    return operations
