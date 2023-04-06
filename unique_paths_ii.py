# You are given an m x n integer array grid. 
# There is a robot initially located at the top-left corner (i.e., grid[0][0]). 
# The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). 
# The robot can only move either down or right at any point in time.

# An obstacle and space are marked as 1 or 0 respectively in grid. 
# A path that the robot takes cannot include any square that is an obstacle.

# Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# The testcases are generated so that the answer will be less than or equal to 2 * 109.

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:

        seenPaths = {}
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        def recordPath(m, n, numPaths):
            seenPaths[f'{m} {n}'] = numPaths
            return numPaths

        def findPaths(m: int, n: int) -> int:
            if f'{m} {n}' in seenPaths: return seenPaths[f'{m} {n}']
            if obstacleGrid[m-1][n-1] == 1:
                return recordPath(m, n, 0)
            if m == 1 and n == 1: 
                return recordPath(m, n, 1)
            if m == 1:
                return recordPath(m, n, findPaths(m, n-1))
            if n == 1:
                return recordPath(m, n, findPaths(m-1, n))
            return recordPath(m, n, findPaths(m-1, n) + findPaths(m, n-1))
        
        return findPaths(m, n)