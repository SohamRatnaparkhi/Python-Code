from collections import Counter
from typing import OrderedDict
word_list = []
for _ in range(int(input())):
    word = input()
    word_list.append(word)
    
word_set = list(OrderedDict.fromkeys(word_list))
print(len(word_set))
c = Counter(word_list)
#ans = []
x = []
for w in word_set:
    
    #ans.append((w, str(c[w])))
    x.append(str(c[w]))

print(" ".join(x))
