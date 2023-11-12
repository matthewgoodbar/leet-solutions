class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''
        parity = True
        while word1 and word2:
            if parity:
                res = res + word1[0]
                word1 = word1[1:]
            else:
                res = res + word2[0]
                word2 = word2[1:]
            parity = not parity
        
        res = res + word1 + word2
        return res