# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
a = set()
for _ in range(n):
    a.add(input())
print(len(a))