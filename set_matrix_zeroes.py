# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

# You must do it in place.

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        rows = []
        columns = []
        
        for idx, row in enumerate(matrix):
            for jdx, entry in enumerate(row):
                if entry == 0: 
                    rows.append(idx)
                    columns.append(jdx)
        
        for row in rows:
            for column in range(len(matrix[0])):
                matrix[row][column] = 0
        
        for column in columns:
            for row in range(len(matrix)):
                matrix[row][column] = 0