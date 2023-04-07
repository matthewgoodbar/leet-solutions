# Given a triangle array, return the minimum path sum from top to bottom.

# For each step, you may move to an adjacent number of the row below. More formally, 
# if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:

        pathRecord = {}

        for level in range(len(triangle)-1, -1, -1):
            for entry in range(len(triangle[level])):
                if level == len(triangle) - 1:
                    pathRecord[(level, entry)] = triangle[level][entry]
                    continue
                minFromEntry = min(pathRecord[(level+1, entry)], pathRecord[(level+1, entry+1)])
                pathRecord[(level, entry)] = triangle[level][entry] + minFromEntry
        
        return pathRecord[(0,0)]