# cook your dish here
def count_factors(n):
    factor = 0
    for i in range(1, n + 1):
        if n % i  == 0:
            factor += 1
    return factor        

for _ in range(int(input())):
    n = int(input())
    '''if count_factors(n) == 2:
        #if prime
        print(n)
        continue'''
    #else:
        #if not prime
        
    factor_list = []
    factors_count = []
    a = []
    for i in range(2,n + 1):
        if n % i == 0:
            k = i
            m =int(n / k) 
            factor_list.append(k)
            factors_count.append(count_factors(m))
        
    maxf = max(factors_count)
    ans = []
    for i in range(len(factor_list)):
        if factors_count[i] == maxf:
            ans.append(factor_list[i])
    print(min(ans))


