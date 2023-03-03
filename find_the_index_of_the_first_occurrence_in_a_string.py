# Given two strings needle and haystack, 
# return the index of the first occurrence of needle in haystack, 
# or -1 if needle is not part of haystack.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needleIdx = hayStart = hayIdx = 0
        match = False
        while hayIdx < len(haystack):
            if haystack[hayIdx] == needle[needleIdx]:
                match = True
                if needleIdx == 0: hayStart = hayIdx
                if needleIdx == len(needle) - 1: return hayStart
                needleIdx += 1
            else:
                needleIdx = 0
                if match:
                    hayIdx = hayStart
                    match = False
            hayIdx += 1
        return -1