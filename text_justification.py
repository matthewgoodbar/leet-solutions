# Given an array of strings words and a width maxWidth, 
# format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

# You should pack your words in a greedy approach; 
# that is, pack as many words as you can in each line. 
# Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

# Extra spaces between words should be distributed as evenly as possible. 
# If the number of spaces on a line does not divide evenly between words, 
# the empty slots on the left will be assigned more spaces than the slots on the right.

# For the last line of text, it should be left-justified, and no extra space is inserted between words.

# Note:

#     A word is defined as a character sequence consisting of non-space characters only.
#     Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
#     The input array words contains at least one word.

class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        lineLen = 0
        currentLine = []
        res = []

        def constructLine(line: list[str], lastLine = False) -> str:
            if lastLine:
                constructedLine = ''
                for word in line:
                    constructedLine += word + ' '
                return constructedLine[:-1].ljust(maxWidth)
            # Only one word in currentLine
            if len(currentLine) < 2:
                constructedLine = currentLine[0].ljust(maxWidth)
                return constructedLine
            # Several words in currentLine
            else:
                numCharacters = sum(len(w) for w in currentLine)
                toFill = maxWidth - numCharacters
                numSpaces = len(currentLine) - 1
                spaces = ['' for i in range(numSpaces)]
                i = 0
                while toFill > 0:
                    spaces[i] += ' '
                    toFill -= 1
                    i += 1
                    if i == len(spaces): i = 0
                constructedLine = ''
                while currentLine:
                    constructedLine += currentLine.pop(0)
                    if spaces:
                        constructedLine += spaces.pop(0)
                return constructedLine

        wordIdx = 0
        for wordIdx in range(len(words)):
            word = words[wordIdx]
            if not currentLine:
                currentLine.append(word)
                lineLen = len(word)
                continue
            # Current word does not break max width
            if lineLen + len(word) + 1 <= maxWidth:
                currentLine.append(word)
                lineLen += len(word) + 1
            # Current word breaks max width
            else:
                res.append(constructLine(currentLine))
                currentLine = [word]
                lineLen = len(word)
        if currentLine:
            res.append(constructLine(currentLine, True))
        return res