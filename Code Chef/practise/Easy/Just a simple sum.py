for _ in range(int(input())):
    (n, m) = map(int, input().split())
    s = 0
    for i in range(1, n + 1):
        s += (i ** i)
    print(s % m)