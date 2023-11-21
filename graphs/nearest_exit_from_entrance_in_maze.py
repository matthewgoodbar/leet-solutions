from collections import deque

class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        
        visited = set()
        visited.add((entrance[0],entrance[1]))
        queue = deque()
        queue.append((entrance[0],entrance[1],0))
        deltas = [(1,0),(0,-1),(-1,0),(0,1)]

        def inRange(i,j):
            return i in range(len(maze)) and j in range(len(maze[0]))
        
        def isExit(i,j):
            return i == 0 or i == len(maze)-1 or j == 0 or j == len(maze[0])-1

        while queue:
            i, j, steps = queue.popleft()
            if steps > 0 and isExit(i,j):
                return steps
            for delta in deltas:
                di, dj = delta
                if (i+di,j+dj) in visited:
                    continue
                if inRange(i+di,j+dj) and maze[i+di][j+dj] == '.':
                    visited.add((i+di,j+dj))
                    queue.append((i+di,j+dj,steps+1))
        
        return -1