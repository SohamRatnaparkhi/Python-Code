from itertools import groupby

s = list(input())

ans = (groupby(s))
a = []
for i,j in ans:
    x = list(j)
    a.append(f"({len(x)},{i})")
                
print(" ".join(a))