class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        n, m = len(text1), len(text2)
        memo = [[0 for _ in range(m+1)] for _ in range(n+1)]

        for i in range(n):
            for j in range(m):
                if text1[i] == text2[j]:
                    memo[i][j] = 1 + memo[i-1][j-1]
                else:
                    memo[i][j] = max(memo[i-1][j], memo[i][j-1])

        return memo[n-1][m-1]

sol = Solution()
t1 = "bsbininm"
t2 = "jmjkbkjkv"
print(sol.longestCommonSubsequence(t1, t2))