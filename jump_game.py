# You are given an integer array nums. 
# You are initially positioned at the array's first index, 
# and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

class Solution:
    def canJump(self, nums: list[int]) -> bool:

        def jumpableFromBeginning(finalIdx):
            if finalIdx == 0:
                return True
            for i in range(finalIdx - 1, -1, -1):
                if nums[i] + i >= finalIdx:
                    return jumpableFromBeginning(i)
            return False
        
        return jumpableFromBeginning(len(nums) - 1)

nums1 = [2,3,1,1,4]
nums2 = [3,2,1,0,4]

sol = Solution()
print(sol.canJump(nums2))