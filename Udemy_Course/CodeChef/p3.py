#test cases
T = int(input())
#input
v  = input()
values = v.split()

N = int(values[0])
Q = int(values[1])

qi = []
for i in range(Q):
    qi.append(int(input()) - 1)

alive = list(range(1, N + 1, 1))
alive_copy = list(range(1, N + 1, 1))
dead = []
l = len(alive)
i = 0
while True:
    i += 1
    
    if i >= len(alive):
        i = 0
        del alive
    
        alive = []
        for num in alive_copy:
            if num in dead:
                continue
            else:
                alive.append(num)
        if l == 1:
            break
        continue

    if i % 2 != 0:
        di = i
        #x = alive_copy.pop(di)

        dead.append(alive[di])
        l -= 1

all_dead = (dead + alive)

for position in qi:
    print(all_dead[position])
