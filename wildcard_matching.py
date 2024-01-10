# ATTEMPT

class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        sLen = len(s)
        pLen = len(p)
        # dp[i][j] => s[:i] matches p[:j]
        dp = [[False for j in range(pLen+1)] for i in range(sLen+1)]
        # empty string matches empty pattern
        dp[0][0] = True
        for i in range(sLen+1):
            for j in range(1,pLen+1):
                # skip j == 0, will always be False
                if i == 0:
                    if all([c == '*' for c in p[:j]]):
                        # when s[:i] is empty (i==0) p[:j] will only match if p[:j] == '*'
                        dp[i][j] = True
                elif p[j-1] == '?' or p[j-1] == s[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]

        return dp[-1][-1]

sol = Solution()
s = 'abcdcd'
p = '*cd'
print(sol.isMatch(s, p))