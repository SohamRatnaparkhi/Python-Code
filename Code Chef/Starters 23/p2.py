'''input
'''
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

def solver():
    #Take input. NO NEED OF TESTCASE LOOP
    x = int(input())
    # Code the question
    ans = f"{x - 1} {x} {x + 1}"
    return ans
    pass

#code ends here
Testcase(solver)