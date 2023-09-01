class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        livingNeighbors = [[0 for j in range(len(board[0]))] for i in range(len(board))]
        deltas = [(1,0),(1,1),(0,1),(-1,1),(0,-1),(-1,-1),(-1,0),(1,-1)]

        def inRange(i,j):
            return i in range(len(board)) and j in range(len(board[0]))

        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 1:
                    for delta in deltas:
                        di, dj = delta
                        if inRange(i+di, j+dj):
                            livingNeighbors[i+di][j+dj] += 1
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                neighbors = livingNeighbors[i][j]
                if board[i][j] == 1:
                    if neighbors < 2 or neighbors > 3:
                        board[i][j] = 0
                else:
                    if neighbors == 3:
                        board[i][j] = 1
                    

sol = Solution()
board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
sol.gameOfLife(board)
print(board)