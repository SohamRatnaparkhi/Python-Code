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

    for i in range(len(matrix)):
        for j in range(1, len(matrix)):
            if matrix[i][j] == 1:
                if checkConnectionHorizontal(matrix[i], j) == False:
                    if checkConnectionVertical(matrix, j, i) == False:
                        matrix[i][j] = 0;
            else : pass

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

    ans = removeIslands(matrix)
    for row in ans:
        print(row)
 
main()