class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        sortedNums = sorted(nums)
        for i in range(len(nums)):
            if sortedNums[i] == sortedNums[i+1]:
                return sortedNums[i]

nums = [1,3,4,2,2]
sol = Solution()
sol.findDuplicate(nums)