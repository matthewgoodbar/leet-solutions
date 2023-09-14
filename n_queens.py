class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:

        def inRange(pos: (int,int)):
            i, j = pos
            return i in range(n) and j in range(n)
        
        def placeQueen(queens, openSquares):

            if len(queens) == n:
                return [buildSolution(queens)]
            
            row = len(queens)
            openSquaresInRow = [square for square in openSquares if square[0] == row]
            if not openSquaresInRow:
                return None
            
            sols = []
            for potentialQueen in openSquaresInRow:
                newOpenSquares = determineOpenSquares(potentialQueen, openSquares)
                newQueens = queens.union({potentialQueen})
                res = placeQueen(newQueens, newOpenSquares)
                if res:
                    sols = sols + res
            return sols


        
        def determineOpenSquares(queen: (int,int), openSquares):
            deltas = [(1,-1), (1,0), (1,1)]
            blacklist = {(queen[0], col) for col in range(n)}
            for delta in deltas:
                i, j = queen
                di, dj = delta
                while inRange((i+di, j+dj)):
                    blacklist.add((i+di,j+dj))
                    i = i+di
                    j = j+dj
            return openSquares.difference(blacklist)
        
        def buildSolution(queens):
            sol = ['' for _ in range(n)]
            for queen in queens:
                row = ''
                for col in range(n):
                    if col == queen[1]:
                        row = row + 'Q'
                    else:
                        row = row + '.'
                sol[queen[0]] = row
            return sol
        
        queens = set()
        openSquares = {(i,j) for i in range(n) for j in range(n)}
        return placeQueen(queens, openSquares)

sol = Solution()
print(sol.solveNQueens(4))