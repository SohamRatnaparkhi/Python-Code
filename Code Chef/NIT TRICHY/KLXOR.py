def subs_create(k, s):
    subs = []
    for i in range(len(s) - k + 1):
        subs.append((s[i: i + k]))
    return subs

def xor(a, b, n):
    ans = ""
     
    # Loop to iterate over the
    # Binary Strings
    for i in range(n):
         
        # If the Character matches
        if (a[i] == b[i]):
            ans += "0"
        else:
            ans += "1"
    return ans

for _ in range(int(input())):
    (n, k) = map(int, input().split())
    s = input()
    ans = ''
    subs = subs_create(k, s)
    if len(subs) == 1:
        ans = subs[0]
    else:
        if len(subs) == 2:
            ans = xor(subs[0], subs[1],k)
        else:
            ans = xor(subs[0], subs[1],k)
            for i in range(2, len(subs)):
                ans = xor(ans, subs[i], k)
    print(ans.count('1'))            

        

    


