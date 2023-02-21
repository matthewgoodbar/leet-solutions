# Given an array nums of distinct integers, return all the possible permutations. 
# You can return the answer in any order.

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        if len(nums) == 1: return [nums]
        prev = self.permute(nums[1:])
        single = nums[0]
        res = []
        for perm in prev:
            for i in range(len(perm)+1):
                permCopy = perm.copy()
                permCopy.insert(i, single)
                res.append(permCopy)
        return res