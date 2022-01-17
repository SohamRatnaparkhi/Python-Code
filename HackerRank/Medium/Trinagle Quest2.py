



for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    s = "".join(list(str(x) for x in range(1, i + 1)))
    e = s[0 : i - 1: 1][::-1]
    print(s + e)





for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print (((10**i - 1)//9)**2)
