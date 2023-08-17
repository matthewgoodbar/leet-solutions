class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:

        currentSet = set()
        accountedFor = set()
        res = [[0 for j in range(len(mat[0]))] for i in range(len(mat))]

        def getNeighbors(indices):
            neighbors = set()
            deltas = [(0,1), (0,-1), (1,0), (-1,0)]
            for (i,j) in indices:
                for (di,dj) in deltas:
                    if i+di in range(len(mat)) and j+dj in range(len(mat[0])):
                        if (i+di,j+dj) not in accountedFor:
                            neighbors.add((i+di,j+dj))
                            accountedFor.add((i+di,j+dj))
            return neighbors


        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    accountedFor.add((i,j))
                    currentSet.add((i,j))
        
        currentDist = 1
        while currentSet:
            neighbors = getNeighbors(currentSet)
            for (i,j) in neighbors:
                res[i][j] = currentDist
            currentSet = neighbors
            currentDist += 1
        
        return res