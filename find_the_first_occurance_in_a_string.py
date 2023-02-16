# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for idx, hay in enumerate(haystack):
            if hay == needle[0]:
                if haystack[idx:idx+len(needle)] == needle: return idx
        return -1