#!/usr/bin/python3
"""
Module for calculating the perimeter of an island.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in a grid.

    Parameters:
        grid: list of list of int

    Returns:
        int: The perimeter of the island.
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:

                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1

                if i == rows - 1 or grid[i + 1][j] == 0:
                    perimeter += 1

                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1

                if j == cols - 1 or grid[i][j + 1] == 0:
                    perimeter += 1

    return perimeter
