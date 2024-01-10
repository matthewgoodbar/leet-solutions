#ATTEMPT
import heapq

class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        n = len(matrix)
        heap = []
        seen = set()
        heapq.heappush(heap, (matrix[0][0], 0, 0))
        seen.add((0,0))
        count = 0
        while count < k:
            current, i, j = heapq.heappop(heap)
            count += 1
            if i+1 < n and (i+1,j) not in seen:
                heapq.heappush(heap, (matrix[i+1][j], i+1, j))
                seen.add((i+1,j))
            if j+1 < n and (i,j+1) not in seen:
                heapq.heappush(heap, (matrix[i][j+1], i, j+1))
                seen.add((i,j+1))
            seen.remove((i,j))
        return current
        


matrix = [[1,5,9],[10,11,13],[12,13,15]]
sol = Solution()
for i in range(1, len(matrix)**2 + 1):
    print(sol.kthSmallest(matrix, i))
# print(sol.kthSmallest(matrix, 8))