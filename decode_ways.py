# A message containing letters from A-Z can be encoded into numbers using the following mapping:

# 'A' -> "1"
# 'B' -> "2"
# ...
# 'Z' -> "26"

# To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). 
# For example, "11106" can be mapped into:

#     "AAJF" with the grouping (1 1 10 6)
#     "KJF" with the grouping (11 10 6)

# Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

# Given a string s containing only digits, return the number of ways to decode it.

# The test cases are generated so that the answer fits in a 32-bit integer.

class Solution:
    def numDecodings(self, s: str) -> int:

        memo = {}

        def countDecodings(s: str) -> int:
            if s == '' or s[0] == '0':
                return 0
            if len(s) == 1:
                return 1
            validRange = range(1, 27)
            if len(s) == 2:
                if s in memo:
                    return memo[s]
                res = 0
                if int(s) in validRange:
                    res += 1
                if int(s[0]) in validRange and int(s[1]) in validRange:
                    res += 1
                memo[s] = res
                return res
            if s in memo:
                return memo[s]
            res = 0
            if int(s[0]) in validRange:
                res += countDecodings(s[1:])
            if int(s[:2]) in validRange:
                res += countDecodings(s[2:])
            memo[s] = res
            return res
        
        return countDecodings(s)