T = int(input())

for g in range(T):
    N = int(input())
    S = list(input())
    P = list(input())

    # Convert ? to u
    index = 0
    st = 0
    for char in S:
        if char == '?':
            
            if P[index] == '?':
                st += 1
            
            S[index] = 'u'

        index += 1
    #print(S)
    index = 0
    for char in P:
        if char == '?':
            P[index] = 'u'
        
        index += 1
    #print(P)

    # Convert P to S
    i = ans =0
    for char in P:
        cs = S[i]
        if cs != char:
            cs = char
            S[i] = cs
            ans += 1
        i += 1

    print (ans + st)
        