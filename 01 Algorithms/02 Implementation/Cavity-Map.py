#!/bin/python3

import sys

def solutionCavityMap (grid):
    n = len(grid)
    for i in range(1, n-1):
        for j in range(1, n-1):
            if grid[i][j+1] != 'X' and int(grid[i][j+1]) < int(grid[i][j]) and \
                grid[i][j - 1] != 'X' and int(grid[i][j - 1]) < int(grid[i][j]) and \
                grid[i - 1][j] != 'X' and int(grid[i - 1][j]) < int(grid[i][j]) and \
                grid[i + 1][j] != 'X' and int(grid[i + 1][j]) < int(grid[i][j]):
                    grid[i][j] = 'X'




n = int(input().strip())
grid = []
grid_i = 0
for grid_i in range(n):
   grid_t = list(input().strip())
   grid.append(grid_t)

solutionCavityMap(grid)
for line in grid:
    print(''.join(line))

