class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroIdx = None
        for i in range(len(nums)):
            if nums[i] == 0:
                zeroIdx = i
                break
        if zeroIdx is None:
            return None
        
        for i in range(zeroIdx+1, len(nums)):
            if nums[i] != 0:
                nums[i], nums[zeroIdx] = nums[zeroIdx], nums[i]
                zeroIdx += 1
        
        return None