# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, 
# nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) 
# such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
# For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, 
# return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if len(nums) == 0: return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        mp = len(nums) // 2
        if nums[mp] == target: return mp
        if nums[mp] > nums[0]: #Inflection in right
            if target in range(nums[0], nums[mp]):
                return self.search(nums[:mp], target)
            else:
                rightSearch = self.search(nums[mp:], target)
                return -1 if rightSearch == -1 else mp + rightSearch
        else: #Inflection in left
            if target in range(nums[mp], nums[-1] + 1):
                rightSearch = self.search(nums[mp:], target)
                return -1 if rightSearch == -1 else mp + rightSearch
            else:
                return self.search(nums[:mp], target)