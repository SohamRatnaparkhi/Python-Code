#test cases
T = int(input())
#input
for i in range(T):
    v  = input()
    values = v.split()

    N = int(values[0]) # Total people
    K = int(values[1]) # Hieght of Gi-Hun and Ali

    v = input()
    val = v.split()
    height = []
    count = 0
    for h in val:
        x = int(h)
        if x > K:
            count += 1

    print(count)



