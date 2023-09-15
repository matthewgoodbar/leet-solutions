# ATTEMPT

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:

        wordSet = set(wordList)
        if beginWord in wordSet:
            wordSet.remove(beginWord)
        minPathMemo = {}

        def oneOff(word1, word2):
            offCount = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    offCount += 1
                if offCount > 1:
                    return False
            return offCount == 1

        def wordStep(currentWord, wordSet):

            print(currentWord)
            print(wordSet)
            print('----------')

            if currentWord in minPathMemo:
                print(f'{currentWord} found in memo: {minPathMemo[currentWord]}')
                print('--------------------')
                return minPathMemo[currentWord]
            
            if oneOff(currentWord, endWord):
                minPathMemo[currentWord] = 1
                print(f'{currentWord} one off from end word {endWord}: {1}')
                print('--------------------')
                return 1
            
            currentMin = 0
            for nextWord in wordSet:
                if oneOff(currentWord, nextWord):
                    res = wordStep(nextWord, wordSet.difference({nextWord}))
                    if res:
                        if currentMin and res + 1 < currentMin:
                            currentMin = res + 1
                        else:
                            currentMin = res + 1
                    print(f'currentMin from {currentWord}: {currentMin}')
            minPathMemo[currentWord] = currentMin
            print(f'final min from {currentWord}: {currentMin}')
            print('--------------------')
            return currentMin
        
        
        return wordStep(beginWord, wordSet)

sol = Solution()
beginWord = 'hit'
endWord = 'cog'
wordList = ["hot","dot","dog","lot","log","cog"]
print(sol.ladderLength(beginWord, endWord, wordList))