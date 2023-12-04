class Solution:
    def numTilings(self, n: int) -> int:
        dp = [0 for _ in range(n+1)]
        for i in range(1,n+1):
            if i == 1:
                dp[i] = 1
            elif i == 2:
                dp[i] = 2
            elif i == 3:
                dp[i] = 5
            else:
                dp[i] = int(((2 * dp[i-1]) + dp[i-3]) % (1e9 + 7))
        return dp[-1]