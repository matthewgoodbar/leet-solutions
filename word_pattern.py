class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        wordMap = {}
        wordPool = set()
        words = s.split(' ')
        if len(words) != len(pattern):
            return False
        for i, char in enumerate(pattern):
            if char in wordMap:
                if wordMap[char] != words[i]:
                    return False
            else:
                if words[i] in wordPool:
                    return False
                wordMap[char] = words[i]
                wordPool.add(words[i])
        return True