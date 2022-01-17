for _ in range(int(input())):
    (n, m) = map(int, input().split())
    seats_row = 0
    
    for i in range(1, m + 1, 2):
        seats_row += 1
    
    if n % 2 != 0:
        #odd
        n += 1

    rows = n / 2
    print(int(rows * seats_row))