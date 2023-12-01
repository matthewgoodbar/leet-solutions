import heapq

class Solution:
    def maxScore(self, nums1: list[int], nums2: list[int], k: int) -> int:
        maxHeap = [(-nums1[i],i) for i in range(len(nums1))]
        heapq.heapify(maxHeap)
        minHeap = []
        kSum = 0
        maxScore = 0

        for i in range(k):
            maxEl, maxIdx = heapq.heappop(maxHeap)
            heapq.heappush(minHeap, (nums2[maxIdx], maxIdx))
            kSum -= maxEl
        
        maxScore = max(maxScore, kSum * minHeap[0][0])
        while maxHeap:
            minEl, minIdx = heapq.heappop(minHeap)
            kSum -= nums1[minIdx]
            maxEl, maxIdx = heapq.heappop(maxHeap)
            kSum -= maxEl
            heapq.heappush(minHeap, (nums2[maxIdx], maxIdx))
            maxScore = max(maxScore, kSum * minHeap[0][0])
        
        return maxScore