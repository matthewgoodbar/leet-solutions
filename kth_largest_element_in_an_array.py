class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:

        maxVal, minVal = None
        for num in nums:
            if not maxVal or minVal:
                maxVal, minVal = num
            else:
                if num > maxVal:
                    maxVal = num
                elif num < minVal:
                    minVal = num
        
        numBuckets = (n // k) + 1
        buckets = []
        currentBucket = {}
        currentBucketCount = 0
        found = False
        passNumber = 0
        while not found:
            bucketRange = range(maxVal-((passNumber+1) * k)+1, maxVal-(passNumber * k)+1)
            for num in nums:
                if num in bucketRange:
                    if num not in currentBucket:
                        currentBucket[num] = 1
                    else:
                        currentBucket[num] += 1
                    currentBucketCount += 1
            
            passNumber += 1