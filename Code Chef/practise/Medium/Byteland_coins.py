
def coin_exchange(n):
    sum = float(n / 2 + n / 3 + n / 4)
    sum_a = float(round(sum))
    d = float(abs(sum_a - sum))
    if d > 0.5:
        sum = int(sum_a) - 1
    else:
        sum = int(sum_a)
    return sum
for T in range(10):
    N = int(input())
    val = coin_exchange(N)
    if val > N:
        print(val)
    else:
        print(N)