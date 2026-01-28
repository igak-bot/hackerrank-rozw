import math
import os
import random
import re
import sys

def superReducedString(s):
    string = list(s)
    index = 0
    while index < (len(string)-1):
        if string[index] == string[index+1]:
            string.pop(index+1)
            string.pop(index)
            index = 0
        else:
            index += 1
    if string == []:
        return 'Empty String'
    else:
        srs = ''.join(string)
        return srs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
