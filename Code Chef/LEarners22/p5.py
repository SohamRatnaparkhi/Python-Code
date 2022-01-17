def even(n):
    if n % 2 == 0:
        return True
    return False

for _ in range(int(input())):
    n = int(input())
    a = input().split()
    
    a.sort()

    median = 0
    mean = sum(a) / n


    if even(n):
        median = a[int(n / 2)]
    else:
        median = a[int((n + 1)/ 2)]

    c = 0
    while mean != median:
        