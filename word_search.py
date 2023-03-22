class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:

        memo = set()
        diffs = [(1,0), (0,1), (-1,0), (0,-1)]

        # Check if word is impossible to construct from the given board
        def countCheck(board, word):
            wordCount = {}
            boardCount = {}
            for char in word:
                if char in wordCount:
                    wordCount[char] += 1
                else:
                    wordCount[char] = 1
            for row in board:
                for char in row:
                    if char in boardCount:
                        boardCount[char] += 1
                    else:
                        boardCount[char] = 1
            
            
            for char in wordCount:
                if char not in boardCount: return False
                if wordCount[char] > boardCount[char]:
                    return False
            return True
            
        # Check if given position is within the bounds of the board
        def inRange(pos):
            x, y = pos
            return x in range(len(board)) and y in range(len(board[0]))

        # DFS starting at pos
        def scour(pos, strIdx):
            x, y = pos
            if (not inRange(pos)) or pos in memo: return False
            if strIdx == len(word) - 1:
                return board[x][y] == word[strIdx]
            
            if board[x][y] == word[strIdx]:
                memo.add(pos)
                for diff in diffs:
                    dx, dy = diff
                    newPos = (x + dx, y + dy)
                    print(word[:strIdx])
                    if inRange(newPos) and (newPos not in memo):
                        if scour(newPos, strIdx + 1): return True
                memo.remove(pos)
                return False
            else:
                return False
            
        if not countCheck(board, word): return False
        
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == word[0] and scour((x, y), 0): return True
        return False

board = [
    ["A","A","A","A","A","A"],
    ["A","A","A","A","A","A"],
    ["A","A","A","A","A","A"],
    ["A","A","A","A","A","A"],
    ["A","A","A","A","A","B"],
    ["A","A","A","A","B","A"]
    ]
word = "AAAAAAAAAAAAABB"
sol = Solution()
print(sol.exist(board, word))