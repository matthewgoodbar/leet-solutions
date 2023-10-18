#ATTEMPT

class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        n = len(matrix)
        heap = []
        


matrix = [[1,5,9],[10,11,13],[12,13,15]]
sol = Solution()
for i in range(1, len(matrix)**2 + 1):
    print(sol.kthSmallest(matrix, i))
# print(sol.kthSmallest(matrix, 8))