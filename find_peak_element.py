class Solution:
    def findPeakElement(self, nums: list[int]) -> int:

        if len(nums) == 1:
            return 0
        
        if nums[0] > nums[1]:
            return 0
        
        if nums[-1] > nums[-2]:
            return len(nums)-1
        
        start = 0
        end = len(nums)-1
        mid = (end + start) // 2

        while start < end:
            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                return mid
            elif nums[mid] < nums[mid+1]:
                start = mid
                mid = (start + end) // 2
            else:
                end = mid
                mid = (start + end) // 2