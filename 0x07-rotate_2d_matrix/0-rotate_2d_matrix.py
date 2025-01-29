#!/usr/bin/python3
'''2D Matrix Rotation Module.

This module provides a function to rotate a square 2D matrix by 90 degrees 
clockwise in-place.
'''

def rotate_2d_matrix(matrix):
    '''Rotates a 2D matrix 90° clockwise in place.

    Args:
        matrix (list of list of int): A square 2D matrix to be rotated.

    Returns:
        None: The matrix is rotated in place, no new matrix is returned.

    This function rotates the matrix in place by performing a series of swaps 
    for each "layer" of the matrix. Each element is moved to its new position 
    as part of a cycle (four elements are swapped at a time).
    '''
    left, right = 0, len(matrix) - 1  # Define the outer bounds of the matrix

    # Loop through the matrix layers (from outermost to innermost)
    while left < right:
        for i in range(right - left):  # Iterate over elements in the current layer
            top, bottom = left, right  # Set the bounds for the current layer

            # Save the value at the top-left corner of the current layer
            topLeft = matrix[top][left + i]

            # Move the bottom-left value to the top-left corner
            matrix[top][left + i] = matrix[bottom - i][left]

            # Move the bottom-right value to the bottom-left corner
            matrix[bottom - i][left] = matrix[bottom][right - i]

            # Move the top-right value to the bottom-right corner
            matrix[bottom][right - i] = matrix[top + i][right]

            # Move the saved top-left value to the top-right corner
            matrix[top + i][right] = topLeft

        # Narrow the bounds for the next inner layer
        right -= 1
        left += 1
