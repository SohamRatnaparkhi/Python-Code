'''input
'''
import sys
import math
import bisect
from sys import stdin,stdout
from math import gcd,floor,sqrt,log
from collections import defaultdict as dd
from bisect import bisect_left as bl,bisect_right as br

sys.setrecursionlimit(100000000)

intip    =lambda: int(input()) #take integer input
strng  =lambda: input().strip() #input without trailing spaced
jn     =lambda x,l: x.join(map(str,l)) #printing a list 'l' with 'x' as deliminator
strl   =lambda: list(input().strip()) #take input and convert to list with list elements as Strings
ip =lambda: map(int,input().strip().split()) #take input elements as int
inpf   =lambda: map(float,input().strip().split())#take input elements as float
inpl    =lambda: list(map(int,input().strip().split()))#take input and convert to list with list elements as int

ceil   =lambda x: int(x) if(x==int(x)) else int(x)+1  #ceiling func on x
ceildiv=lambda x,d: x//d if(x%d==0) else x//d+1 #ceiling func in (x / d)

flush  =lambda: stdout.flush()
stdstr =lambda: stdin.readline()
stdint =lambda: int(stdin.readline())
stdpr  =lambda x: stdout.write(str(x))

mod=1000000007


#main code
