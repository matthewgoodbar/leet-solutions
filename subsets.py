# Given an integer array nums of unique elements, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        if len(nums) <= 1: return [[], nums]
        prev = self.subsets(nums[1:])
        leftOver = nums[0]
        res = [subset for subset in prev]
        for subset in prev:
            newSubset = subset.copy()
            newSubset.append(leftOver)
            newSubset.sort()
            res.append(newSubset)
        return res