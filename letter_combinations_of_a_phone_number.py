class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if len(digits) == 0:
            return []
        
        def getLetters(digit: str):
            if digit == '2':
                return ["a","b","c"]
            elif digit == '3':
                return ["d","e","f"]
            elif digit == '4':
                return ['g','h','i']
            elif digit == '5':
                return ['j','k','l']
            elif digit == '6':
                return ['m','n','o']
            elif digit == '7':
                return ['p','q','r','s']
            elif digit == '8':
                return ['t','u','v']
            else:
                return ['w','x','y','z']
        
        if len(digits) == 1:
            return getLetters(digits[0])
        
        prev = self.letterCombinations(digits[1:])
        res = []
        for letter in getLetters(digits[0]):
            for combo in prev:
                res.append(letter + combo)
        return res