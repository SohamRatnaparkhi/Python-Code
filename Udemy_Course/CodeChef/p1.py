# cook your dish here
T = int(input())
for i in range(T):
    v = input()
    s = 0
    for c in v:
        s += 1
        if c == ' ':
            space = int(s)
            break
    n = []
    k = []
    for i in range(space):
        n.append(v[i])

    for i in range(space, len(v), 1):
        k.append(v[i])
        
    n1 = ''.join(n)
    k1 = ''.join(k)

    N = int(n1)
    K = int(k1)

    for i in range(K):
        if N % 10 == 9:
            #end with 9
            N -= 9
            
        
        else:
            N += 1
            
    print(N)
