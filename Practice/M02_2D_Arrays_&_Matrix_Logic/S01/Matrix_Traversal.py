from typing import List
def diagonalSum(self, mat: List[List[int]]) -> int:
    n = len(mat)
    s = 0 
    for i in range(n):
        for j in range(n):
            if i == j :
                s += mat[i][j]
            if i + j == n-1:
                s += mat[i][j]
    if  n%2==1:
        s -= mat[n//2][n//2]
    return s
mat = [[1,2,3],[4,5,6],[7,8,9]]
print(diagonalSum(mat))     