    
N = int(input())
num_list = list(map(int, input().split()))
Q = int(input())
def sum_index(l, x, y):
    sum = 0
    for i in range(x,y + 1):
            sum += l[i]
    return sum
            
for i in range(Q):
        (x, y) =  (map(int, input().split()))
        ans = sum_index(num_list, x, y)
        print(ans)


