# A phrase is a palindrome if, 
# after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
# it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        def sanitize(s: str) -> str:
            alphabet = set("abcdefghijklmnopqrstuvwxyz0123456789")
            string = s.lower()
            for char in s:
                if char not in alphabet: string = string.replace(char, "")
            return string
        
        def palindrome(s: str) -> bool:
            mp = len(s) // 2
            if len(s) % 2 == 0:
                return s[:mp] == s[-1:mp-1:-1]
            else:
                return s[:mp] == s[-1:mp:-1]
        
        return palindrome(sanitize(s))