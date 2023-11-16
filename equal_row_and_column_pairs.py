class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        n = len(grid)
        rows = {}
        for row in grid:
            tRow = tuple(row)
            if tRow in rows:
                rows[tRow] += 1
            else:
                rows[tRow] = 1
        
        count = 0
        for j in range(n):
            column = tuple([grid[i][j] for i in range(n)])
            if column in rows:
                count += rows[column]
        
        return count