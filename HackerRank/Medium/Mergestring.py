from typing import OrderedDict
def merge_the_tools(string, k):
    # your code goes here
    n = len(string)
    x = int(n / k)
    t = []
    for i in range(0, len(string), k):
        t.append(string[i : i + k])
    print(len(t))
    for word in t:
        h = list(word)
        w = list(OrderedDict.fromkeys(h))
        
        print(''.join(w))
        
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)