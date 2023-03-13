# Given an unsorted integer array nums, return the smallest missing positive integer.

# You must implement an algorithm that runs in O(n) time and uses constant extra space.

class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        possibleMissing = set(range(1, len(nums)+2))
        for num in nums:
            if num in possibleMissing: possibleMissing.remove(num)
        return min(possibleMissing)