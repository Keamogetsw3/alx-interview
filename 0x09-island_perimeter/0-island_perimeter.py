#!/usr/bin/python3
"""
Defines a function to calculate the perimeter of an island in a grid
"""


def island_perimeter(grid):
    """Calculate and return the perimeter of an island in a grid.

    Args:
        grid: A 2D list representing a grid where:
            - '1' represents land,
            - '0' represents water.

    Returns:
        int: The perimeter of the island
    """
    height = len(grid)
    width = len(grid[0])
    edges = 0
    size = 0

    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1:
                if j > 0 and grid[i][j - 1] == 1:
                    edges += 1
                if i > 0 and grid[i - 1][j] == 1:

                    edges += 1 
    perimeter = size * 4 - edges * 2
    return perimeter
