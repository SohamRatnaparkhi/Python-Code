
"""contents = open("D:\\Soham\\test.txt.docx", mode='w')
contents.write("New line through editor")
with open('D:\\Soham\\test.txt.docx', mode='a') as f:
    f.writelines("Soham")
with open('D:\\Soham\\test.txt.docx', mode='r') as f:
    print(f.read())

with open('D:\\Soham\\test.txt.docx', mode='a') as f:
    f.writelines("\nSoham")
with open('D:\\Soham\\test.txt.docx', mode='r') as f:
    print(f.read())

with open('new_file.txt', mode='w') as f:
    f.writelines("I CREATED THE FILE")
with open('new_file.txt', mode='r') as f:
    print(f.read())
if (1<2 and 2>3):
    print("true")
elif (3 == 3):
    print("3")"""

# print words starting with s
"""
st = 'Print only the words that start with s in this sentence'
mylist  = st.split()
#print (mylist)

for word in mylist:
    if word[0] == 's':
        print(word)
"""

#range func to genr. 0 to 10 snd print even nos
"""
mylist = list(range(0, 10, 2))
print(mylist)
"""

#list comprehension to no. diveidibel by 3 btwn 1 an 50
"""
mylist = list(range(0, 50, 1))
newlist = [x for x in mylist if x % 3 == 0]
print(newlist)
"""

#print letter with enven length
"""
st =  input("Enter a string - ")
word_list = st.split()
for word in word_list:
    l = len(word)
    if l % 2 == 0:
        print(word)
"""

#print first letter of every word
"""
st =  input("Enter a string - ")
i = 0
final_ans = []
word_list = st.split()
for word in word_list:
    ch = word[0]
    final_ans.append(ch)  

print(final_ans)
"""