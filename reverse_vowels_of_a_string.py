class Solution:
    def reverseVowels(self, s: str) -> str:
        vowelStack = []
        vowels = {'a','e','i','o','u','A','E','I','O','U'}

        for char in s:
            if char in vowels:
                vowelStack.append(char)
        
        res = ''
        for char in s:
            if char in vowels:
                res = res + vowelStack.pop()
            else:
                res = res + char
        
        return res

s = 'hello'
sol = Solution()
print(sol.reverseVowels(s))