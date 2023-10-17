#ATTEMPT

class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        n = len(matrix)
        diagLen = 1
        diag = 0
        while k > diagLen:
            k -= diagLen
            if diag >= n-1:
                diagLen -= 1
            else:
                diagLen += 1
            diag += 1
            # print(f'k: {k}, diag: {diag}, diagLen: {diagLen}')
        # print(f'target is in diagonal {diag}')
        if diag < n:
            diagElements = [matrix[i][diag-i] for i in range(diagLen)]
        else:
            diagElements = [matrix[diag-n+1+i][n-1-i] for i in range(diagLen)]
        return sorted(diagElements)[k-1]


matrix = [[1,5,9],[10,11,13],[12,13,15]]
sol = Solution()
for i in range(1, len(matrix)**2 + 1):
    print(sol.kthSmallest(matrix, i))
# print(sol.kthSmallest(matrix, 8))