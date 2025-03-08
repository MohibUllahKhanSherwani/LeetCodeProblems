
# Given an m x n matrix, return all elements of the matrix in spiral order.
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# for i in range(len(matrix)):
#             for j in range(len(matrix[i])):
#                 print(matrix[i][j], end = ' ')  
#             print('')
# Approach: m = rows = matrix.length
#           n = columns = matrix[i].length

from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        traversed = []
        rows = len(matrix)
        columns = len(matrix[0])
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        while left < right and top < bottom: 
            #Get every i in the top row
            for i in range(left, right):
                traversed.append(matrix[top][i])
            top += 1   
            #Get every i in the right col
            for i in range(top, bottom):
                traversed.append(matrix[i][right - 1])
            right -= 1
            if len(traversed) == (rows * columns):
                break
            for i in range(right - 1, left - 1, -1):
                traversed.append(matrix[bottom - 1][i])
            bottom -= 1
            for i in range(bottom - 1, top - 1, - 1):
                traversed.append(matrix[i][left])
            left += 1
        return traversed
matrix = [[1,2,3],[4,5,6],[7,8,9]]
s = Solution()
print('Traversed array: ', s.spiralOrder(matrix))