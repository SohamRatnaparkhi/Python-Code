#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#
def win_loss(a, b):
    if a > b: return"A"
    elif a < b: return"B"
    else: return "T"

def compareTriplets(a, b):
    # Write your code here
    alice = 0
    bob = 0

    for i in range(len(a)):
        
        x = a[i]
        y = b[i]

        if win_loss(x, y) == "A":
            alice += 1
        elif win_loss(x, y) == "B":
            bob += 1
        else: 
            pass
    result = [alice, bob]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

