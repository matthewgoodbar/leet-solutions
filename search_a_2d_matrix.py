# You are given an m x n integer matrix matrix with the following two properties:

#     Each row is sorted in non-decreasing order.
#     The first integer of each row is greater than the last integer of the previous row.

# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        #BSearch for row
        row = self.findRow(matrix, target)
        print(row)

        #BSearch for element
        return self.bsearch(row, target)
        
    def findRow(self, matrix, target) -> list:
        if len(matrix) <= 1: return matrix[0]
        midpoint = len(matrix) // 2
        if target < matrix[midpoint][0]:
            return self.findRow(matrix[:midpoint], target)
        else:
            return self.findRow(matrix[midpoint:], target)
    
    def bsearch(self, row, target) -> bool:
        if len(row) == 0: return False
        if len(row) == 1:
            return True if row[0] == target else False
        midpoint = len(row) // 2
        if row[midpoint] == target: return True
        if target < row[midpoint]: return self.bsearch(row[:midpoint], target)
        else: return self.bsearch(row[midpoint:], target)

mat = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
sol = Solution()
print(sol.searchMatrix(mat, 3))