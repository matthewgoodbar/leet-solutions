class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        currentGroup = set()
        mapped = set()
        deltas = [(0,1),(1,0),(0,-1),(-1,0)]

        def onBorder(i, j):
            for delta in deltas:
                di, dj = delta
                if i+di not in range(len(board)) or j+dj not in range(len(board[0])):
                    return True
            return False
        
        def inRange(i, j):
            return i in range(len(board)) and j in range(len(board[0]))

        def mapGroup(i, j):
            capturable = True
            currentGroup.add((i,j))
            mapped.add((i,j))
            if onBorder(i,j):
                capturable = False
            neighbors = [(i+di,j+dj) for (di,dj) in deltas]
            for neighbor in neighbors:
                neighborI, neighborJ = neighbor
                if not inRange(neighborI, neighborJ):
                    continue
                if neighbor in currentGroup:
                    continue
                if board[neighborI][neighborJ] == 'O':
                    neighborCapturable = mapGroup(neighborI, neighborJ)
                    if not neighborCapturable:
                        capturable = False
            return capturable
        
        def captureGroup(group):
            for (i,j) in currentGroup:
                board[i][j] = 'X'
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O' and (i,j) not in mapped:
                    capturable = mapGroup(i, j)
                    if capturable:
                        captureGroup(currentGroup)
                    currentGroup = set()  