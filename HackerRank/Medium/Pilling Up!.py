def greater(a, b):
    if a < b:
        return b
    return a
for _ in range(int(input())):
    n = int(input())
    blocks = list(map(int, input().split()))
    game = True
    i = 0
    if len(blocks) == 2:
            game = True
    else:        
        while game:
            up = blocks.pop(0)
            down = blocks.pop(len(blocks) - 1)
            big = greater(up, down)
            
            if i == 0 and len(blocks) > 5:
                i += 1
                continue
            else:
                if big >= blocks[0] or big >= blocks[len(blocks)-1]:
                    game = True
                else:
                    game = False
                    break
            if len(blocks) <= 2:
                game = True
                break
            
    if game:
        print("YES")
    else: 
        print("NO")