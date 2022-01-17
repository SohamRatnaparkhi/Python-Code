

import math
import os
import random
import re
import sys
from collections import Counter

def letter_count(s):
    c= Counter(s)
    return c.most_common()

if __name__ == '__main__':
    s = input()
    l = letter_count(s)
    
    if l[0][1] == 1:
        l.sort()
        
    else:
        pass
        # l = l[0 : 3]
    i = 0
    do_once = True
    while i < 3:
        
        
        if do_once == True:
            if l[0][1] == l[0 + 1][1]:
                if do_once == True:
                    t = 1
                    for j in range(len(l) - 1):
                        if l[j][1] == l[j + 1][1]:
                            t += 1
                        else:
                            break
                    x = l[0 : t]
                    y = l[t : len(l)]
                    x.sort()
                    l = x + y
                    do_once = False

            #x  = l.pop(0)
            #print(f"{x[0]} {x[1]}")

        x  = l.pop(0)
        print(f"{x[0]} {x[1]}")
        i += 1
