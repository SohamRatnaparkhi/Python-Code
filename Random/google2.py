def checkConnectionHorizontal(r, j):
    row = list(r)
    for i in range(j - 1, -1, -1):
        if row[i] != 1:
            for k in range(j + 1, len(row), 1):
                if row[k] != 1:
                    return False
        
    return True
def checkConnectionVertical(matrix, j, k):
    for i in range(k - 1, -1, -1):
        if matrix[i][j] != 1:
            for z in range(k + 1, len(matrix)):
                if matrix[z][j] != 1:
                    return False
    return True

def removeIslands(matrix):
    for i in range(len(matrix) - 1):
        for j in range(1, len(matrix) - 1):
            if matrix[i][j] == 1:
                if checkConnectionHorizontal(matrix[i], j) == True or checkConnectionVertical(matrix, j, i) == True:
                    continue
                elif checkConnectionHorizontal(matrix[i], j) == False and (matrix[i - 1][j] == 1 or matrix[i + 1][j] == 1):
                    u = i - 1
                    up = None
                    d = i + 1
                    down = None
                    while (u >= 0 and matrix[u][j] == 1):
                        if checkConnectionHorizontal(matrix[u], j) == True:
                            up = True
                            break
                        else:
                            u -= 1
                            up = False
                    if up == False or up == None:
                        while (d < len(matrix) and matrix[d][j] == 1):
                            if checkConnectionHorizontal(matrix[d], j) == True:
                                down = True
                                break
                            else:
                                d += 1
                                down = False
                    
                    if up != True and down != True:
                        matrix[i][j] = 0
                elif checkConnectionHorizontal(matrix[i], j) == False and checkConnectionVertical(matrix, j, i) == False:
                    matrix[i][j] = 0
                    continue
    return matrix

def main():
    matrix = [ 
                [1,0,0,0,0,0],
                [0,1,0,1,1,1],
                [0,0,1,0,1,0],
                [1,1,0,0,1,0],
                [1,0,1,1,0,0],
                [1,0,0,0,0,1]
             ]
    matrix2 = [ 
                [1,0,0,0,1,0],
                [0,1,1,1,1,0],
                [0,1,1,1,1,0],
                [0,1,1,1,1,0],
                [0,0,0,0,0,0],
                [1,0,0,0,0,1]
             ]

    ans = removeIslands(matrix)
    for row in ans:
        print(row)
 
main()