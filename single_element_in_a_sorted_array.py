# You are given a sorted array consisting of only integers where every element appears exactly twice, 
# except for one element which appears exactly once.

# Return the single element that appears only once.

# Your solution must run in O(log n) time and O(1) space.

class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        if len(nums) == 1: return nums[0]
        mp = len(nums) // 2
        if nums[mp] == nums[mp-1]:
            left = nums[:mp+1]
            right = nums[mp+1:]
            toSearch = left if len(left) % 2 == 1 else right
        elif nums[mp] == nums[mp+1]:
            left = nums[:mp]
            right = nums[mp:]
            toSearch = left if len(left) % 2 == 1 else right
        else:
            return nums[mp]
        return self.singleNonDuplicate(toSearch)