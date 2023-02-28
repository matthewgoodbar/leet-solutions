# Given an array of strings strs, group the anagrams together. 
# You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        sortedWords = {}
        for string in strs:
            sortedWord = str(sorted(list(string)))
            if sortedWord not in sortedWords:
                sortedWords[sortedWord] = [string]
            else:
                sortedWords[sortedWord].append(string)
        return list(sortedWords.values())