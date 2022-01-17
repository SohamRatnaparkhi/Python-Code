#test cases
for _ in range(int(input())):
    #program starts
    (n, k, s) = map(int, input().split())
    if k == 1:
        break
    s2 = sum(list(range(1, n * 2, 2)))
    ans = (s - s2) / (k - 1)
    print(int(ans))