#!/bin/python3

import math
import os
import random
import re
import sys
from typing import Counter



#
# Complete the 'numCells' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY grid as parameter.
#

def numCells(grid):
    # Write your code here
    n = []
    m = []
    for neigbours in grid:
        individual = max(neigbours)
        n.append(individual)
    m = len(n)
    return(m)
        # for individuals in neigbours:
        #     print(individuals)
grid = [[1, 2, 7], [4, 5, 6], [8, 8, 9]]
print(numCells(grid))
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     grid_rows = int(input().strip())
#     grid_columns = int(input().strip())

#     grid = []

#     for _ in range(grid_rows):
#         grid.append(list(map(int, input().rstrip().split())))

#     result = numCells(grid)

#     fptr.write(str(result) + '\n')

#     fptr.close()
