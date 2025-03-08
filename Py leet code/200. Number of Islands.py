# Given an m x n 2D binary grid grid which represents a map of '1's (land) 
# and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by 
# connecting adjacent lands horizontally or vertically. 
# You may assume all four edges of the grid are all surrounded by water.

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1

# Approach: Take rows and columns as len(grid) and len(grid[0])
# initialize a count variable = 0
# then run for loops i in range(rows) and then inside it j in range(columns)
# if you encounter a 1 increase the count variable, then call dfs(i, j) method to 
# conduct a depth first search on it
# inside the dfs method check if (i or j are not inside bounds or if grid[i][j] != 1)
# if true simply return, if it not true then mark the current grid[i][j] = 0
# call dfs on its all 4 neighbours
from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        print ('Rows: ', rows, 'Columns: ', columns)
        total_islands = 0
        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= columns or grid[i][j] != '1':
                return
            grid[i][j] = 0 # Mark it as water(0) so we dont again count it
            dfs(i + 1, j) # Next row
            dfs(i, j + 1) # Next column
            dfs(i - 1, j) # Prev row
            dfs(i, j - 1) # Prev column
                
        for i in range(rows):
            for j in range(columns):
                if (grid[i][j] == '1'):
                    total_islands += 1
                    dfs(i, j)

        return total_islands
 
s = Solution()
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print('Islands: ', s.numIslands(grid))