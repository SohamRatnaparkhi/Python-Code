# Test cases
T = int(input())
def sum_list(l):
        sum = 0
        for i in l:
            sum += i

        return sum
# number of elements in list
for a in range(T):
    N = int(input())
    # sting - v list - A with space seperated value
    v = input()
    #val = v.split()
    A = list(map(int,v.split()))
    
    
       # a_copy.append(int(h))
    
    j = 0
    sum_l = []
    for num in A:
        a_copy = []
        for g in A:
            a_copy.append(g)
        x = a_copy.pop(j)
        s = sum_list(a_copy)
        sum_l.append(s)
        j += 1
        del a_copy

    sum_l.sort()
    max = sum_l[len(sum_l)-1] 
        

    print(max)

