# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        if len(nums) == 1: return [nums]
        prev = self.permuteUnique(nums[1:])
        single = nums[0]
        res = []
        for perm in prev:
            for i in range(len(perm)+1):
                permCopy = perm.copy()
                permCopy.insert(i, single)
                if permCopy not in res: res.append(permCopy)
        return res