#tails = 1
#heads = 0
import time
start = time.time()
def flip(s):
    if s == '0':
        return '1'
    return '0'    

(N, Q) = map(int, input().split())
coins = list('1' * N)

for i in range(Q + 1):
    (check, ub, lb) = map(int, input().split())
    if check == 0:
        #flip coins
        for j in range(ub, lb + 1):
            coins[j] = flip(coins[j])

    elif check == 1:
        #count heads
        head = 0
        for j in range(ub, lb + 1):
            if coins[j] == '0':
                head += 1
        print(head)
end = time.time()
print(start - end)

