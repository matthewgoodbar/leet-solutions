# Write a program to solve a Sudoku puzzle by filling the empty cells.

# A sudoku solution must satisfy all of the following rules:

#     Each of the digits 1-9 must occur exactly once in each row.
#     Each of the digits 1-9 must occur exactly once in each column.
#     Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

# The '.' character indicates empty cells.

class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def validPlacement(row, col, num):
            for i in range(9):
                if board[row][i] == num: return False
                if board[i][col] == num: return False
                if board[3*(row//3) + i//3][3*(col//3) + i%3] == num: return False
            return True
        
        def checkPlacement(row, col):
            if row > 8:
                return True
            if col > 8:
                return checkPlacement(row + 1, 0)
            
            if board[row][col] != '.':
                return checkPlacement(row, col + 1)
            else:
                for i in range(1,10):
                    if validPlacement(row, col, str(i)):
                        # If valid, check the rest of the board
                        board[row][col] = str(i)
                        if checkPlacement(row, col + 1): 
                            # There is a solution for the rest of the board
                            return True
                        else: 
                            # No solution for rest of the board
                            board[row][col] = '.'
                # No number 1-9 works for this row, col
                return False
        
        checkPlacement(0,0)