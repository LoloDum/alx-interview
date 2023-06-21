#!/usr/bin/python3
"""
Island Perimeter:
    returns the perimeter of the island described in grid
"""


def island_perimeter(grid):
    """island perimenter function"""
    perimeter = 0
    for a in range(len(grid)):
        for b in range(len(grid[a])):
            if grid[a][b] == 1:
                perimeter += 4
                if a > 0 and grid[a-1][b] == 1:
                    perimeter -= 2
                if b > 0 and grid[a][b-1] == 1:
                    perimeter -= 2
    return perimeter
