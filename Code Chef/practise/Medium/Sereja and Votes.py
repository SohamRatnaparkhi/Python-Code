for _ in range(int(input())):
    n = int(input())
    b = list(map(int, input().split()))
    c = 0
    for i in b:
        if i > 0:
            c += 1
    s = sum(b)
    if s == 100:
        print("YES")
    elif s < 100:
        print("NO")
    else:
        if  s - c < 100:
            print("YES")         
        else:
            print("NO")