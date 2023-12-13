class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        # dp[i][j] = distance between first i letters of word1
        # and first j letters of word2
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        # when either word1 or word2 is empty string (when i or j is 0)
        # distance is just the length of the other (n or m insertions)
        for i in range(n+1):
            dp[i][0] = i
        for j in range(m+1):
            dp[0][j] = j
        
        for i in range(1,n+1):
            for j in range(1,m+1):
                if word1[i-1] == word2[j-1]:
                    # when last char in word1 and word2 are equal
                    # it's the same distance as if those last chars
                    # were not there, i.e. dp[i-1][j-1]
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # when last char in word1 and word2 are not equal
                    # we "swap" to make them equal, hence 1+
                    # plus the minimum distance between the previous chars
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

        return dp[-1][-1]

sol = Solution()
word1 = 'horse'
word2 = 'ros'
print(sol.minDistance(word1,word2))