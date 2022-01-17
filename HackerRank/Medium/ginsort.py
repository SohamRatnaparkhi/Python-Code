s = list(input())
nums_odd = []
nums_even = []
upper = []
lower = []
for i in s:
    try:
        x = int(i)
        if x % 2 == 0:
            nums_even.append(str(x))
        else:
            nums_odd.append(str(x))
    except :
        if i.isupper():
            upper.append(i)
        else:
            lower.append(i)
nums_even.sort()
nums_odd.sort()
upper.sort()
lower.sort()
print(lower)
print(upper)

print("".join(lower) + "".join(upper) + "".join(nums_odd) +"".join(nums_even))
        