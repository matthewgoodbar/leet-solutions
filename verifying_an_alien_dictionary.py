class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:

        alphaSet = set()
        for i in range(len(order)-1):
            for j in range(i+1, len(order)):
                alphaSet.add((order[i],order[j]))
        
        def compare(word1, word2):
            # return True if word1 lexicographically preceeds word 2, else False
            for i in range(min(len(word1),len(word2))):
                if (word1[i],word2[i]) in alphaSet:
                    return True
                elif word1[i] == word2[i]:
                    continue
                else:
                    return False
            
            if len(word1) <= len(word2):
                return True
            return False
        
        for i in range(len(words)-1):
            if not compare(words[i],words[i+1]):
                return False
        return True
    
sol = Solution()
order = "hlabcdefgijkmnopqrstuvwxyz"
words = ["hello","leetcode"]
print(sol.isAlienSorted(words, order))