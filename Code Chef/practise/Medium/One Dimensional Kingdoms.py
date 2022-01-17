    for _ in range(int(input())):
        n = int(input())
        kingdom = []
        kingdom_area = []
        intersection = 0
        for __ in range(n):
            bounds = list(map(int, input().split()))
            kingdom.append(bounds)
            area = list(range(bounds[0], bounds[1] + 1))
            kingdom_area.append(area)
            kingdom.sort()
        for i in range(n):
            for j in range(i + 1, n):
                if kingdom[i][1] >= kingdom[j][0]:
                    intersection += 1
        if intersection > 1:
            bomb = n - intersection + 1
        else:
            bomb = n - intersection
        print(bomb)

        


