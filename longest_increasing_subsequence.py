class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:

        memo = {}
        
        def getLongestFromHere(idx):

            if idx in memo:
                return memo[idx]

            if idx == len(nums) - 1:
                memo[idx] = [nums[idx]]
                return memo[idx]

            subs = []
            for jdx in range(idx+1, len(nums)):
                if nums[jdx] > nums[idx]:
                    subs.append(getLongestFromHere(jdx))
            if subs:
                res = [nums[idx]] + max(subs, key=lambda x: len(x))
            else:
                res = [nums[idx]]
            memo[idx] = res
            return memo[idx]
        
        res = [getLongestFromHere(i) for i in range(len(nums))]
        return len(max(res, key=lambda x: len(x)))

sol = Solution()
nums = [10,9,2,5,3,7,101,18]
print(sol.lengthOfLIS(nums))