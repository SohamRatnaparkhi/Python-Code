(N, X, Y) = map(int, input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))



work_a = []
work_b = []
wa = 1
wb = 1
for i in range(N):
    
    if (A[i] > B[i]) and wa <= X:
        work_a.append(A[i])
        wa += 1
    elif (A[i] < B[i]) and wb <= Y:
        work_b.append(B[i])
        wb += 1
    else:
        if wa <= X:
            work_a.append(A[i])
            wa += 1
        elif wb <= Y:
            work_b.append(B[i])
            wb += 1
    

def sum_list(l):
    sum = 0
    for i in l:
        sum += i
    return sum

a = work_a + work_b
print(sum_list(a))
