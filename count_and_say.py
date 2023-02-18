# The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

#     countAndSay(1) = "1"
#     countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.

# To determine how you "say" a digit string, split it into the minimal number of substrings such that each substring contains exactly one unique digit. 
# Then for each substring, say the number of digits, then say the digit. 
# Finally, concatenate every said digit.

# Given a positive integer n, return the nth term of the count-and-say sequence.

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1: return "1"
        prev = self.countAndSay(n-1)

        starts = [0]
        for idx, char in enumerate(prev):
            if idx == 0: continue
            if char != prev[idx-1]: starts.append(idx)

        subStrings = []
        if len(starts) == 1:
            subStrings.append(prev)
        else:
            for idx, start in enumerate(starts):
                if idx == len(starts) - 1:
                    subStrings.append(prev[start:])
                else:
                    subStrings.append(prev[start:starts[idx+1]])
        res = ""
        for sub in subStrings:
            res += str(len(sub)) + sub[0]
        return res

sol = Solution()
print(sol.countAndSay(5))