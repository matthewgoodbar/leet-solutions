# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal substring consisting of non-space characters only.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = 0
        pointer = -1
        while s[pointer] == " ":
            pointer -= 1
        while pointer >= -1 * len(s) and s[pointer] != " ":
            l += 1
            pointer -= 1
        return l