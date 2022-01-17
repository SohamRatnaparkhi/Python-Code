#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonal_Difference(arr, l):
    # Write your code here
    d1 = 0
    for i in range(l):
        d1 += arr[i][i]
    
    return d1        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonal_Difference(arr, len(arr))

    fptr.write(str(result) + '\n')

    fptr.close()
    