class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a','e','i','o','u'}
        start = 0
        end = k-1
        currentCount = 0
        for char in s[:k]:
            if char in vowels:
                currentCount += 1
        maxVowels = currentCount
        
        while end < len(s)-1:
            if s[start] in vowels:
                currentCount -= 1
            start += 1
            end += 1
            if s[end] in vowels:
                currentCount += 1
            if currentCount > maxVowels:
                maxVowels = currentCount
        
        return maxVowels