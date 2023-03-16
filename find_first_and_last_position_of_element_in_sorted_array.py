# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        if not nums: return [-1,-1]

        def bsearch(nums, target, start):
            if not nums: return -1
            if len(nums) == 1 and nums[0] != target: return -1
            mp = len(nums) // 2
            if start: # Looking for starting index
                if nums[mp] == target and (mp == 0 or nums[mp-1] != target):
                    return mp
                if target <= nums[mp]:
                    # Search left
                    return bsearch(nums[:mp], target, start)
                else:
                    # Search right
                    right = bsearch(nums[mp:], target, start)
                    return -1 if right == -1 else right + mp
            else: # Looking for ending index
                if nums[mp] == target and (mp == len(nums) - 1 or nums[mp+1] != target):
                    return mp
                if target < nums[mp]:
                    # Search left
                    return bsearch(nums[:mp], target, start)
                else:
                    # Search right
                    right = bsearch(nums[mp:], target, start)
                    return -1 if right == -1 else right + mp
            
        
        return [bsearch(nums, target, True), bsearch(nums, target, False)]