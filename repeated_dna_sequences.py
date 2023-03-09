
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:

        if len(s) < 10: return []

        subSequences = set()
        res = []

        for i in range(len(s) - 9):
            subSeq = s[i:i+10]
            if subSeq in subSequences:
                if subSeq not in res: res.append(subSeq)
            else:
                subSequences.add(subSeq)
        
        return res

s = 'AAAAAAAAAAA'
sol = Solution()
print(sol.findRepeatedDnaSequences(s))