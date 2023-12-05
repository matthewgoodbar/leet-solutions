from collections import deque
import heapq

class Solution:
    def totalCost(self, costs: list[int], k: int, candidates: int) -> int:
        queue = deque(costs)
        leftHeap = []
        rightHeap = []
        totalCost = 0

        while queue and (len(leftHeap) < candidates and len(rightHeap) < candidates):
            heapq.heappush(leftHeap, queue.popleft())
            if queue:
                heapq.heappush(rightHeap, queue.pop())

        for _ in range(k):
            if (leftHeap and not rightHeap) or (leftHeap and leftHeap[0] <= rightHeap[0]):
                totalCost += heapq.heappop(leftHeap)
                if queue:
                    heapq.heappush(leftHeap, queue.popleft())
            elif (rightHeap and not leftHeap) or (rightHeap and leftHeap[0] > rightHeap[0]):
                totalCost += heapq.heappop(rightHeap)
                if queue:
                    heapq.heappush(rightHeap, queue.pop())
        
        return totalCost




sol = Solution()
costs = [57,33,26,76,14,67,24,90,72,37,30]
k = 11
candidates = 2
print(sol.totalCost(costs, k, candidates))