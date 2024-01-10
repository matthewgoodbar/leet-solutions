class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2
        dp = [[False for j in range(target+1)] for i in range(len(nums)+1)]
        dp[0][0] = True
        for i in range(1,len(nums)+1):
            for j in range(target+1):
                if j == 0 or dp[i-1][j]:
                    dp[i][j] = True
                elif j - nums[i-1] >= 0 and dp[i-1][j-nums[i-1]]:
                    dp[i][j] = True
                if j == target and dp[i][j]:
                    return True
        return dp[-1][-1]

sol = Solution()
nums = [1,5,11,5]
sol.canPartition(nums)