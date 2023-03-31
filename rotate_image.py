# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
# DO NOT allocate another 2D matrix and do the rotation.

class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def quadSwap(i, j):
            size = len(matrix)
            i2, j2 = j, size - i - 1
            i3, j3 = j2, size - i2 - 1
            i4, j4 = j3, size - i3 - 1
            temp = matrix[i4][j4]
            matrix[i4][j4] = matrix[i3][j3]
            matrix[i3][j3] = matrix[i2][j2]
            matrix[i2][j2] = matrix[i][j]
            matrix[i][j] = temp
            

        for ring in range(len(matrix)//2):
            ringLength = len(matrix) - (2 * ring)
            for start in range(ring, ring + ringLength -1):
                quadSwap(ring, start)