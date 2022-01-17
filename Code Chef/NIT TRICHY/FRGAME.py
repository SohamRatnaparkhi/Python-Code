def add_one(a, b, c):
    if b > a:
        #Nitin loss
        a += c
    else:
        b += c
    return (a,b)
def win(a, b):
    if b > a:
        return 'S'
    return "N"
for _ in range(int(input())):
    (a, b, c, d) = map(int, input().split())
    (a2, b2) = add_one(a, b, c)
    if b2 > a2:
        #Nitin loss
        a2 += d
    else:
        b2 += d
    print(win(a2, b2))
    
        

    
    