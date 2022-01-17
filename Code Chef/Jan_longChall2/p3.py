'''input
'''
from operator import indexOf
import os
import sys
from io import BytesIO, IOBase
import math
import bisect
from sys import stdin,stdout
from math import gcd,floor,sqrt,log
from collections import defaultdict as dd
from bisect import bisect_left as bl,bisect_right as br

sys.setrecursionlimit(100000000)


def main():
    pass


# region fastio

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._file = file
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

# endregion
inpi    =lambda: int(input()) #take integer input
strng  =lambda: input().strip() #input without trailing spaces
jn     =lambda x,l: x.join(map(str,l)) #printing a list 'l' with 'x' as deliminator
strl   =lambda: list(input().strip()) #take input and convert to list with list elements as Strings
ip =lambda: map(int,input().strip().split()) #take input elements as int
inpf   =lambda: map(float,input().strip().split())#take input elements as float
intl    =lambda: list(map(int,input().strip().split()))#take input and convert to list with list elements as int

ceil   =lambda x: int(x) if(x==int(x)) else int(x)+1  #ceiling func on x
ceildiv=lambda x,d: x//d if(x%d==0) else x//d+1 #ceiling func in (x / d)

flush  =lambda: stdout.flush()
stdstr =lambda: stdin.readline()
stdint =lambda: int(stdin.readline())
stdpr  =lambda x: stdout.write(str(x))

mod=1000000007



if __name__ == "__main__":
    main()

# Searching algorithms
def BinarySearchAsc(l, target, s, e):
    """Searches a target element in array using binary search algorithm

    Args:
        l ([list]): [Array sorted in ascending order]
        target ([int]): [element to be searched]

    Returns:
        [integer]: [index of target element if it is found else - 1]
    """
    

    while(s <= e):
        mid = int(s + (e - s) / 2)
        
        if l[mid] > target:
            e = mid - 1
        elif l[mid] < target:
            s = mid + 1
        else:
            
            return mid
    return -1

def BinarySearchDesc(l, target, s, e):
    """Searches a target element in array using binary search algorithm

    Args:
        l ([list]): [Array sorted in descending order]
        target ([int]): [element to be searched]

    Returns:
        [integer]: [index of target element if it is found else - 1]
    """
    s = 0
    e = len(l) - 1 

    while s <= e:
        mid = int(s + (e - s) / 2)
            
        if l[mid] > target:
            s = mid + 1
        elif l[mid] < target:
            e = mid - 1
        else:
            return mid
    return -1
    
#Testcase
def Testcase(func):
    n = int(input())
    for i in range(n):
        print(func())

#code starts here
def check_2(a, b, n, i, j):
    
    return int(n - a[i])
    pass

def check_3(r, g, b, n):
    bag = [r, g, b]
    ans = 0
    while r[0] < n or g[1] < n or b[2] < n :
        '''
        m1 = max(r) 
        i1 = indexOf(r, m1)
        m2 = max(b)
        i2 = indexOf(b, m2)
        m3 = max(g) 
        i3 = indexOf(g, m3)
        big = max(m1, m2, m3)
        zero = -1
        val = n - big '''

        if r[0] < n:
            if g[0] > 0 and r[1] > 0:
                g[0] -= 1
                r[0] += 1  # r <-> g (1)  g[0] goes to r[0] and r[1] goes to g[1] 
                           #  so basically 1 red from basket_2 swaps with 1 green in basket_1
                g[1] += 1
                r[1] -= 1
                ans += 1
            elif b[0] > 0 and r[2] > 0:
                b[0] -= 1
                r[0] += 1   # b[0] goes to r[0] 

                b[2] += 1  # r[2] goes to b[2]
                r[2] -= 1 
                ans += 1    # basically 1 blue from basket_1 swaps with 1 red from basket_3

        if g[1] < n:
            if r[1] > 0 and g[0] > 0:
                r[1] -= 1
                g[1] += 1   # r[1] goes to g[1]

                g[0] -= 1   # g[0] goes to r[0]
                r[0] += 1
                ans += 1    # basically green from basket_1 swaps with one red from basket_2
            elif b[1] > 0 and g[2] > 0:
                b[1] -= 1 
                g[1] += 1   # b[1] goes to g[1]

                g[2] -= 1   # g[2] goes to b[2]
                b[2] += 1
                ans += 1 # basically green from basket_2 swaps with blue of basket_2 
            
        if b[2] < n:
                if r[2] > 0 and b[0] > 0:         # r[2] -> b[2] and b[0] -> r[0]
                    r[2] -= 1
                    b[2] += 1

                    b[0] -= 1
                    r[0] += 1
                    ans += 1
                elif g[2] > 0 and b[2] > 0 and b[1] > 0:      # g[2] -> b[2] and b[1] -> g[1]
                    g[2] -= 1
                    b[2] += 1

                    b[1] -= 1
                    g[1] += 1   
                    ans += 1  
                elif r[0] == n-1 and g[1] == n-1 and b[2] == n-1 and r[2] == 0 and g[0] == 0 and b[1] == 0:
                    return ans +  n - g[1]
                else:
                    x = min(r[0], g[1], b[2])
                    cnt = 0
                    for i in [r[0], g[1], b[2]]:
                        if i == x:
                            cnt += 1
                    return ans + n - x + ((n-x) * cnt)
    return ans
    pass    

def solver():
    #Take input. NO NEED OF TESTCASE LOOP
    n = inpi()
    (r1, g1, b1) = ip()
    (r2, g2, b2) = ip()
    (r3, g3, b3) = ip()

    red_bag = [r1, g1, b1]
    green_bag = [r2, g2, b2]
    blue_bag = [r3, g3, b3]

    ans = 0

    # Code the question
    if r1 == n and g2 == n and b3 == n:
        return 0
    elif r1 == n and g2 != n and b3 != n:
        ans = check_2(green_bag, blue_bag, n, 1, 2)
    elif r1 != n and g2 == n and b3 != n:
        ans = check_2(red_bag, blue_bag, n, 0, 2)
    elif r1 != n and g2 != n and b3 == n:
        ans = check_2(red_bag, green_bag, n, 0, 1)
    else:
        ans = check_3(red_bag, green_bag, blue_bag, n)
    return ans
    pass

#code ends here
Testcase(solver)