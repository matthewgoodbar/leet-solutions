# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
#     Each row must contain the digits 1-9 without repetition.
#     Each column must contain the digits 1-9 without repetition.
#     Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Look through rows
        for row in board:
            valid = self.validGroup(row)
            if not valid: return False
        
        #Look through columns
        for i in range(9):
            column = []
            for j in range(9):
                column.append(board[j][i])
            valid = self.validGroup(column)
            if not valid: return False

        #Look through quadrants
        quads = [1, 4, 7]
        difs = [-1, 0, 1]
        for i in quads:
            for j in quads:
                #i, j is quad center
                quad = []
                for k in difs:
                    for l in difs:
                        quad.append(board[i+k][j+l])
                valid = self.validGroup(quad)
                if not valid: return False

        return True
    
    def validGroup(self, group):
        count = {}
        for space in group:
            if space not in count: count[space] = 1
            else: count[space] += 1
        del count["."]
        counts = list(count.values())
        for value in counts:
            if value != 1: return False
        return True