# Given an integer array nums where every element appears three times except for one, which appears exactly once. 
# Find the single element and return it.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        d = {}
        for num in nums:
            if num in d:
                if d[num]:
                    del d[num]
                else:
                    d[num] = True
            else:
                d[num] = False
        return list(d.keys())[0]