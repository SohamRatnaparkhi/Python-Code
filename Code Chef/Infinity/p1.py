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
    
    A.sort()
    n = A.pop(0)
    max = sum_list(A)
        

    print(max)

