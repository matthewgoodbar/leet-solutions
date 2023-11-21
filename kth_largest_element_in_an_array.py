import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:

        heapq.heapify(nums)
        
        for i in range(len(nums)-k):
            heapq.heappop(nums)
        
        return heapq.heappop(nums)