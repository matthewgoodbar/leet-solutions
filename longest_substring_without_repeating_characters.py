# Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "": return 0
        seenCharacters = {}
        longest = [0, 0]
        start = 0
        for idx, char in enumerate(s):
            if char in seenCharacters and (seenCharacters[char] >= start):
                start = seenCharacters[char] + 1
            if idx - start > longest[1] - longest[0]:
                longest = [start, idx]
            seenCharacters[char] = idx
        return longest[1] - longest[0] + 1