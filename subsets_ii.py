# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        if len(nums) == 1: return [[], nums]
        oddOut = nums[0]
        prev = self.subsetsWithDup(nums[1:])
        new = [sorted(subset + [oddOut]) for subset in prev]
        for subset in new:
            if subset not in prev: prev.append(subset)
        return prev