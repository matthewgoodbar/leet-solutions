# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        prevRow = self.getRow(rowIndex - 1)
        res = [1]
        for i in range(len(prevRow) - 1):
            res.append(prevRow[i] + prevRow[i+1])
        res.append(1)
        return res