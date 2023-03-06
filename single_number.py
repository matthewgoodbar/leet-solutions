# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        d = {}
        for num in nums:
            if num in d:
                del d[num]
            else:
                d[num] = True
        return list(d.keys())[0]