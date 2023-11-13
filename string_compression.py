class Solution:
    def compress(self, chars: list[str]) -> int:
        currentChar = chars[0]
        currentCount = 1
        insertIdx = 0
        for i in range(1, len(chars)+1):
            if i == len(chars) or chars[i] != currentChar:
                if currentCount > 1:
                    currentRes = currentChar + str(currentCount)
                    for char in currentRes:
                        chars[insertIdx] = char
                        insertIdx += 1
                else:
                    chars[insertIdx] = currentChar
                    insertIdx += 1
                if i < len(chars):
                    currentChar = chars[i]
                currentCount = 1
            else:
                currentCount += 1
        return insertIdx