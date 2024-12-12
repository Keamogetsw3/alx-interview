#!/usr/bin/python3
"""Island Perimeter Problem
"""

def island_perimeter(grid):
    """
    Calculates the perimeter of the island described in grid.
    
    Args:
        grid (list[list[int]]): 2D grid of integers where 0 represents water and 1 represents land.
    
    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows, cols = len(grid), len(grid[0]) if grid else 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check top
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                # Check bottom
                if i == rows - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                # Check left
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                # Check right
                if j == cols - 1 or grid[i][j + 1] == 0:
                    perimeter += 1
    return perimeter
