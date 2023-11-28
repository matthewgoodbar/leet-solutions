class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        memo = {}

        def findLongest(i, j):
            if (i,j) in memo:
                return memo[(i,j)]
            if i == len(text1) or j == len(text2):
                return 0
            if text1[i] == text2[j]:
                res = 1 + findLongest(i+1, j+1)
                memo[(i,j)] = res
                return res
            else:
                res = max(findLongest(i+1,j), findLongest(i,j+1))
                memo[(i,j)] = res
                return res
        
        return findLongest(0,0)