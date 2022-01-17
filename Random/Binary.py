def dec_bin(x):
    rem = []
    while (x != 0):
        y = int(x % 2)
    # print(f"2 | {x}     | {y}")
        x = int(x / 2)
        z = str(y)
        rem.append(z)

    s = ''.join(rem)

    #print(bin(x))
    #print("---------")

    return (s[::-1])

x = input()
p = 0
if '.' in x:
    
    for i in range(len(x)):
        if x[i] == '.':
            p = i
            break
    y = []
    for i in range(p):
        y.append(x[i])

    g = ''.join(y)
    d = int(g)
    
    #print(d)
    r  = dec_bin(d)
    print(f"Not an integer, but binary representation of fractional part is {r}")

else:
    d = int(x)

    #print(d)
    r  = dec_bin(d)
    print(r)

def bin_dec(n):
    x = n[::-1]
    dec = 0
    for i in range(len(x)):
        digit = (int(x[i]))
        power = int((2 ** i))
        dec += power * digit
    return dec

x = input()
dec = bin_dec(x)

print(dec)

