import itertools
def generate_bitwise_and(l):
    bitwise_and = []
    '''
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            d = l[i]&l[j]
            bitwise_and.append(d)

    '''
    for (i, j) in itertools.combinations(l,2):
        d =  i&j
        bitwise_and.append(d)
    return bitwise_and


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = generate_bitwise_and(a)
    
    while len(b) > 1 :
        
        b.sort()
        
        x = b.pop(0)
        y = b.pop(len(b) - 1)
        r = x | y
        b.append(r)
        #a = b

    print(b[0])


