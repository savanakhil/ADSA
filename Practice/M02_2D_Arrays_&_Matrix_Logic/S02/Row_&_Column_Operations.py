'''1531. Count Negative Numbers in a Sorted Matrix'''
from typing import List
def countNegatives(grid: List[List[int]]) -> int:
    count = 0
    for row in grid:
        for num in row:
            if num < 0:
                count += 1
    return count
grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
print(countNegatives(grid))
'''OR'''
from typing import List
def countNegatives(grid: List[List[int]]) -> int:
    count = 0
    row = len(grid)
    col = len(grid[0])  
    for i in range(row):
        for j in range(col):
            if grid[i][j] < 0:
                count += 1
    return count
grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
print(countNegatives(grid))