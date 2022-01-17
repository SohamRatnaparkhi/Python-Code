for _ in range(int(input())):
    (z, y , a, b, c) = map(int, input().split())
    money = z - y
    if a + b +c <= money:
        print("YES")
    else:
        print("NO")
