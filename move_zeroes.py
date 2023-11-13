class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        queue = []
        for num in nums:
            if num != 0:
                queue.append(num)
        
        for i in range(len(nums)):
            if queue:
                nums[i] = queue.pop(0)
            else:
                nums[i] = 0
        
        return None