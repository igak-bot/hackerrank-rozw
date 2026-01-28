import math
import os
import random
import re
import sys
from operator import truediv


def commonChild(s1, s2):
    l = len(s1)
    grid = [[0] * (l+1) for i in range(l+1)]

    for i in range(1, l+1):
        for j in range(1, l+1):
            if s1[i-1] == s2[j-1]:
                grid[i][j] = grid[i-1][j-1] + 1
            else:
                grid[i][j] = max(grid[i-1][j], grid[i][j-1])
    return max(max(grid))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()