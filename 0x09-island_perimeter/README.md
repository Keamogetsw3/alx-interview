# 0x09. Island Perimeter

## Overview

The "0. Island Perimeter" project requires you to calculate the perimeter of an island within a grid. The grid is represented as a 2D list of integers, where:
- `1` represents land,
- `0` represents water.

The task is to compute the perimeter of a single island, which is defined by its land cells (`1`). The island may be surrounded by water or touch the edge of the grid, and your job is to determine how many edges of the island's cells are exposed to water.

## Project Details

- **Weight:** 1
- **Start Date:** Dec 2, 2024, 6:00 AM
- **End Date:** Dec 6, 2024, 6:00 AM
- **Checker Release:** Dec 3, 2024, 6:00 AM
- **Auto Review:** Launched at the deadline.

## Task Description

You are tasked with creating an algorithm to calculate the perimeter of an island in a 2D grid. 

### Key Concepts:
- **2D Arrays (Matrices):** You will need to iterate over the 2D grid, accessing adjacent cells horizontally and vertically.
- **Conditional Logic:** Apply conditions to check if a land cell contributes to the perimeter.
- **Counting Edges:** Count the exposed edges of the island, which are the edges of land cells that are either at the border of the grid or adjacent to water.

### Problem Breakdown:
1. Identify the land cells in the grid.
2. For each land cell, check its four adjacent cells (up, down, left, right).
3. If any adjacent cell is water (`0`) or out of bounds (i.e., the land cell is at the edge of the grid), increase the perimeter count.
4. The goal is to calculate the total perimeter by summing the contributions from all land cells.

## Requirements

- **General:**  
    - Allowed editors: vi, vim, emacs
    - All your files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.4.3).
    - All your files should end with a new line.
    - The first line of all your files should be exactly `#!/usr/bin/python3`.
    - A `README.md` file is mandatory at the root of the project folder.
    - Code should follow **PEP 8** style (version 1.7).
    - You are not allowed to import any external modules.
    - All modules and functions must be documented.
    - All your files must be executable.

## Function Signature

```python
def island_perimeter(grid: list[list[int]]) -> int:
    """Returns the perimeter of the island represented in the grid."""
