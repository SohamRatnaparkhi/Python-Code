def even(n):
    if n % 2 == 0:
        return True
    return False
for _ in range(int(input())):
    (n, x, y) = map(int, input().split())
    
    cx = (n + 1) / 2
    cy = (n + 1) / 2

    coin =0

    if even(x) and not even(y):
        coin = 1
    elif not even(x) and not even(y):
        coin = 0
    elif even(x) and even(y):
        coin = 0
    elif not even(x) and even(y):
        coin = 1

    print(coin)

    