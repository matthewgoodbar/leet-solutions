#ATTEMPT

class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2

        def buildSubset(nums, target):
            for num in nums:
                if num == target:
                    return True
            for i in range(len(nums)):
                if buildSubset(nums[:i]+nums[i+1:], target-nums[i]):
                    return True
            return False
        
        return buildSubset(nums, target)