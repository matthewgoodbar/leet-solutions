class Solution:
    def decodeString(self, s: str) -> str:
        res = ''

        pointer = 0
        multiplier = None
        while pointer < len(s):
            char = s[pointer]
            if char.isnumeric():
                if not multiplier:
                    multiplier = char
                else:
                    multiplier += char
            elif char == '[':
                bracketStack = 0
                subPointer = pointer + 1
                subRes = ''
                while True:
                    subChar = s[subPointer]
                    if subChar == '[':
                        subRes += subChar
                        bracketStack += 1
                    elif subChar == ']':
                        if bracketStack == 0:
                            break
                        else:
                            subRes += subChar
                            bracketStack -= 1
                    else:
                        subRes += subChar
                    subPointer += 1
                subRes = self.decodeString(subRes)
                res += int(multiplier)*subRes
                multiplier = None
                pointer = subPointer
            else:
                res += char
            pointer += 1

        return res