from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:

        deltas = [(1,0),(0,1),(-1,0),(0,-1)]
        fresh = set()

        rotted = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rotted.append((i,j,0))
                elif grid[i][j] == 1:
                    fresh.add((i,j))
        
        minute = 0
        while rotted:
            i, j, minute = rotted.popleft()
            for delta in deltas:
                di, dj = delta
                if (i+di,j+dj) in fresh:
                    rotted.append((i+di,j+dj,minute+1))
                    fresh.remove((i+di,j+dj))
        
        if fresh:
            return -1
        return minute