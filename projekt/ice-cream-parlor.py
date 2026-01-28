import math
import os
import random
import re
import sys

def icecreamParlor(m, arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j:
                price1 = arr[i]
                price2 = arr[j]
                total = price1 + price2
                if total == m:
                    return (i + 1), (j + 1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        m = int(input().strip())

        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
