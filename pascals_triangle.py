# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        triangle = [[1]]
        if numRows == 1: return triangle
        for i in range(numRows - 1):
            newRow = [1]
            prevRow = triangle[-1]
            for j in range(1,len(prevRow)):
                newRow.append(prevRow[j] + prevRow[j-1])
            newRow.append(1)
            triangle.append(newRow)
        return triangle