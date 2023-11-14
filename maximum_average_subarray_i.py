class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        start = 0
        end = k-1
        currentSum = 0
        for i in range(start, end+1):
            currentSum += nums[i]
        maxAverage = currentSum / k

        while end < len(nums)-1:
            currentSum -= nums[start]
            start += 1
            end += 1
            currentSum += nums[end]
            if currentSum / k > maxAverage:
                maxAverage = currentSum / k
        
        return maxAverage