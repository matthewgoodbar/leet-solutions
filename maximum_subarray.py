# Given an integer array nums, find the subarray with the largest sum, and return its sum.

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxSum = 0
        currentSum = 0
        maxSinglet = None
        for num in nums:
            # Record the single least negative number in nums
            # in case all of nums is < 0
            if maxSinglet == None:
                maxSinglet = num
            else:
                if num > maxSinglet: maxSinglet = num
            # Add num to running sum, restart sum if
            # adding num results in negative sum
            if currentSum + num < 0:
                currentSum = 0
            else:
                currentSum += num
                if currentSum > maxSum: maxSum = currentSum
        return maxSum if maxSinglet >= 0 else maxSinglet