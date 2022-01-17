def check_code(s):
    c1 = 0
    for i in range(len(s) - 7):
        if s[i] == 'c':
            if s[i + 1] == 'o' and s[i + 2] == 'd'and s[i + 3] == 'e':
                c1 = i
                return ("True", c1)
            else:
                continue
    return ("False", c1)

def check_chef(s, c1):
    for i in range(c1 + 4, len(s) - 3):
        if s[i] == 'c':
            if s[i + 1] == 'h' and s[i + 2] == 'e'and s[i + 3] == 'f':
                return "AC"
    return "WA"
def chef1(s):
    ch1 = 0
    for i in range(len(s)):
        if s[i] == 'c':
            if s[i + 1] == 'h' and s[i + 2] == 'e'and s[i + 3] == 'f':
                ch1 = i
                return ("True", ch1)
    return ("False", ch1)

for _ in range(int(input())):
    n = int(input())
    s = list(input())
    
    (result_code, c1) = check_code(s)
    (result_chef, ch1) = chef1(s)
    if result_code == "True" and result_chef == "True" and c1 + 3 < ch1:
        if result_code == "True":
            print(check_chef(s, c1))
        else:
            print('WA')
    else:
        print('WA')        
