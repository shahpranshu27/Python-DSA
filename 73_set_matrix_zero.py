# matrix=[[1,1,1],[1,0,1],[1,1,1]]
matrix = [[1,2,0],[3,4,2],[0,1,5]]

m = len(matrix)
n = len(matrix[0])

for i in range(m):
    for j in range(n):
        # print(matrix[i][j])
        if matrix[i][j] == 0:
            for col in range(n):
                if matrix[i][col] != 0:
                    matrix[i][col] = -1
            
            # print("col marked -1 ===== ", matrix)
            
            for row in range(m):
                if matrix[row][j] != 0:
                    matrix[row][j] = -1
            
            # print("row marked -1 ===== ", matrix)
            
# print("-1 matrix ------ ", matrix)
for i in range(m):
    for j in range(n):
        if matrix[i][j] == -1:
            matrix[i][j] = 0

for row in matrix:
    print(row)