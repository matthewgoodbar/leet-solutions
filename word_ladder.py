from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:

        wordSet = set(wordList)
        if beginWord in wordSet:
            wordSet.remove(beginWord)
        if endWord not in wordSet:
            return 0

        def oneOff(word1, word2):
            offCount = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    offCount += 1
                if offCount > 1:
                    return False
            return offCount == 1
        
        queue = deque()
        queue.append((beginWord,1))
        while queue:
            current, dist = queue.popleft()
            oneAway = set()
            for word in wordSet:
                if oneOff(current, word):
                    if word == endWord:
                        return dist+1
                    oneAway.add(word)
                    queue.append((word, dist+1))
            wordSet = wordSet.difference(oneAway)
        return 0

        

sol = Solution()
beginWord = 'hit'
endWord = 'cog'
wordList = ["hot","dot","dog","lot","log","cog"]
print(sol.ladderLength(beginWord, endWord, wordList))