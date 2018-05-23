#
# ps8pr3.py  (Problem Set 8, Problem 3)
#
# Conway's Game of Life
#
# Computer Science 111  
#

# IMPORTANT: this file is for your solutions to Problem 3.
# Your solutions to Problem 2 should go in ps8pr2.py instead.

from ps8pr2 import *
from gol_graphics import *
import random

# a function that may be useful when testing your other functions
def random_grid(height, width):
    """ creates and returns a height x width grid in which the inner cells
        are randomly set to 0 or 1, and cells on the outer border are all 0.
        inputs: height and width are positive integers
    """
    grid = create_grid(height, width)   # initially all 0s
 
    for r in range(1, height - 1):
        for c in range(1, width - 1):
            grid[r][c] = random.choice([0, 1])
            
    return grid

def count_neighbors(cellr, cellc, grid):
    """ returns the number of alive neighbors of the cell at position
    [cellr][cellc] in the specified grid """
    count = 0
    for r in range(cellr-1, cellr+2):
        for c in range(cellc-1, cellc+2):
            if r != cellr or c != cellc:
                if grid[r][c] == 1:
                    count += 1
    return count

def next_gen(grid):
    """ rules of the Game of Life to create and return a new 2-D list
    representing the next generation of cells """
    new_grid = create_grid(len(grid), len(grid[0]))
    for r in range(len(new_grid)):
        for c in range(len(new_grid[0])):
            if r != 0 and c != 0 and r != len(grid) - 1 and c != len(grid[0]) - 1:
                if count_neighbors(r, c, grid) < 2 or count_neighbors(r, c, grid) > 3:
                    new_grid[r][c] = 0
                elif count_neighbors(r, c, grid) == 3 and grid[r][c] == 0:
                    new_grid[r][c] = 1
                else:
                    new_grid[r][c] = grid[r][c]
    return new_grid
                    
