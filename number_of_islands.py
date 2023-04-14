# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
# You may assume all four edges of the grid are all surrounded by water.

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        islandCount = 0
        seenTiles = set()

        diffs = [(1,0),(0,1),(-1,0),(0,-1)]
        def mapIsland(i, j):
            seenTiles.add((i,j))
            for delta in diffs:
                di, dj = delta
                if i + di in range(len(grid)) and j + dj in range(len(grid[0])):
                    if grid[i + di][j + dj] == "1" and (i + di, j + dj) not in seenTiles:
                        mapIsland(i + di, j + dj)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in seenTiles:
                    mapIsland(i, j)
                    islandCount += 1
        
        return islandCount