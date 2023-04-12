# Given a set of distinct positive integers nums, 
# return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

#     answer[i] % answer[j] == 0, or
#     answer[j] % answer[i] == 0

# If there are multiple solutions, return any of them.

class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        nums.sort()
        dp = [[num] for num in nums]

        for i in range(len(nums)):
            biggestDivisibleSubset = None
            for j in range(i):
                subset = dp[j]
                if nums[i] % subset[-1] == 0:
                    if biggestDivisibleSubset is None:
                        biggestDivisibleSubset = j
                    else:
                        if len(dp[j]) >= len(dp[biggestDivisibleSubset]):
                            biggestDivisibleSubset = j
            if biggestDivisibleSubset is not None:
                dp[i] = dp[biggestDivisibleSubset] + dp[i]
            print(dp)
        
        return max(dp, key=len)

sol = Solution()
nums = [1,2,4,8]
sol.largestDivisibleSubset(nums)