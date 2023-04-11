# Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        dpArray = [[0 for j in range(cols)] for i in range(rows)]

        maxSquare = 0
        for i in range(rows):
            for j in range(cols):
                if i == 0 or j == 0:
                    dpArray[i][j] = int(matrix[i][j])
                    if dpArray[i][j] == 1 and maxSquare == 0:
                        maxSquare = 1
                elif matrix[i][j] == '0':
                    dpArray[i][j] = 0
                else:
                    entry = min(dpArray[i-1][j], dpArray[i][j-1], dpArray[i-1][j-1]) + 1
                    if entry > maxSquare:
                        maxSquare = entry
                    dpArray[i][j] = entry
        
        return maxSquare * maxSquare