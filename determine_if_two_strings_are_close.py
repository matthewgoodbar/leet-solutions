class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        def getCounts(s):
            res = {}
            for char in s:
                if char in res:
                    res[char] += 1
                else:
                    res[char] = 1
            return res
        
        counts1 = getCounts(word1)
        counts2 = getCounts(word2)
        
        return set(counts1) == set(counts2) and sorted(list(counts1.values())) == sorted(list(counts2.values()))