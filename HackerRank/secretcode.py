def is_prime(n):
    for i in range(2, int(n)):
        if n % i == 0:
            return False
    return True
for _ in range(int(input())):
    z = int(input())
    #prime = [2]
    p1 = 2
    p2 = 0
    ans = []
    # cnt = 1
    
    for i in range(3, int(z / 2)):
        if is_prime(i):
           # prime.append(i)
            p2 = i
            if p1 * p2 <= z:
                ans.append(p1 * p2)
            (p1, p2) = (p2, p1) 
    
    
    print(max(ans))

        
        