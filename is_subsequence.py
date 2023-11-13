class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if len(s) > len(t):
            return False
        
        if s == '':
            return True
        
        sPointer = 0
        
        for char in t:
            if char == s[sPointer]:
                sPointer += 1
                if sPointer == len(s):
                    return True
        
        return False