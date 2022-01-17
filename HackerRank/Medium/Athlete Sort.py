#!/bin/python3

import math
import os
import random
import re
import sys


def generate_random(l):
    return max(l) + 1

def sort_generator(all_keys, arr, k):
    d = {}
    
    c = 0
    for i in range(len(l)):
        for j in range( len(l) - 1):
            if i != j:
                if l[i] == l[j]:
                    c += 1
                    #l[i] = generate_random(l)
    for i in range(len(arr)):
        group = arr[i]
        key = l[i]
        
        d[key] = group
     
    return (d,l)

def sort_wrt_key(key_arr, d, k):
    key_arr.sort()
    
    ans = []
    for key in key_arr:
        ans.append((d[key]))
    
    return ans




if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    all_keys = []
    i = 0
    for group in arr:
        all_keys.append(group[k])

    (d,t) = sort_generator(all_keys, arr, k)
    ans = sort_wrt_key(t, d, k)
    
    for a in ans:
        x = [str(z) for z in a]
        #print(x)
        #s = "".split(x)
        print(" ".join(x))