#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the time_delta function below.
# Format - Day dd Mon yyyy hh:mm:ss +xxxx

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the time_delta function below.
# Format - Day dd Mon yyyy hh:mm:ss +xxxx

def return_time(t):
    x = str(t)
    c = x.split(":")
    return (int(c[0]), int(c[1]), int(c[2]))

def time_delta(t1, t2):
    
    day_dict = {"Mon": 1, "Tue": 2, "Wed": 3, "Thu": 4, "Fri": 5, "Sat": 6, "Sun": 7}
    month_dict = {"Jan": 31, "Feb": 28, "Mar": 31, "Apr": 30, "May": 31, "Jun": 30, "Jul": 31, "Aug": 31, "Sep": 30, "Oct": 31, "Nov": 30, "Dec": 31}
    t1 = t1
    t2 = t2
    #day = [day_dict[t1[0]], day_dict[t2[0]]]
    date = [int(t1[1]), int(t2[1])]
    month = [month_dict[t1[2]], month_dict[t2[2]]]
    year = [int(t1[3]), int(t2[3])]
    
    c1 = return_time(t1[4])
    c2 = return_time(t2[4])

    tz1 = t1[5]
    tz2 = t2[5]
    tzh1 = int(tz1[1:3])
    tzh2 = int(tz2[1:3])
    tzm1 = int(tz1[-2:])
    tzm2 = int(tz2[-2:])
    hour = [c1[0], c2[0]]
    mins = [c1[1], c2[1]]
    seconds = [c1[2], c2[2]]

    if tz1[0] == '+' and tz2[0] == '+':
        hour = [c1[0] - tzh1, c2[0] - tzh2]
        mins = [c1[1] - tzm1, c2[1] - tzm2]
        sec = [c1[2], c2[2]]
    elif tz1[0] == '-' and tz2[0] == '-':
        hour = [c1[0] + tzh1, c2[0] + tzh2]
        mins = [c1[1] + tzm1, c2[1] + tzm2]
        seconds = [c1[2], c2[2]]
    elif tz1[0] == '+' and tz2[0] == '-':
        hour = [c1[0] - tzh1, c2[0] + tzh2]
        mins = [c1[1] - tzm1, c2[1] + tzm2]
        seconds = [c1[2], c2[2]] 
    elif tz1[0] == '-' and tz2[0] == '+':
        hour = [c1[0] + tzh1, c2[0] - tzh2]
        mins = [c1[1] + tzm1, c2[1] - tzm2]
        seconds = [c1[2], c2[2]] 
    
    #daydiff = day[0] - day[1]
    datediff = date[0] - date[1]
    monthdiff = month[0] - month[1]
    yeardiff = year[0] - year[1]
    hourdiff = hour[0] - hour[1]
    minsdeff = mins[0] - mins[1]
    secondsdeff = seconds[0] - seconds[1]
    
    deltal = yeardiff * 31536000 + (monthdiff + datediff * 24 * 3600) + hourdiff * 3600 +minsdeff * 60 + secondsdeff 
    return abs(deltal)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input().split()

        t2 = input().split()

        delta = str(time_delta(t1, t2))

        fptr.write(delta + '\n')
        #s = '\n'.join(map(str, delta))
        #fptr.write(s)

    fptr.close()

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input().split()

        t2 = input().split()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
