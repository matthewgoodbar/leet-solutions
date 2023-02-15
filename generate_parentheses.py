# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        if n == 1: return ["()"]
        previous = self.generateParenthesis(n - 1)
        new = []
        for prevParen in previous:
            for i, char in enumerate(prevParen):
                newParen = prevParen[:i] + "()" + prevParen[i:]
                if newParen not in new: new.append(newParen)
        return new