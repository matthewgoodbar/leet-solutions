# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        commonPrefix = ""
        i, allMatching = 0, True
        while allMatching:
            if all(i in range(len(word)) for word in strs):
                commonChar = strs[0][i]
            else:
                break
            if all(word[i] == commonChar for word in strs):
                commonPrefix += commonChar
            else:
                allMatching = False
            i += 1
        return commonPrefix