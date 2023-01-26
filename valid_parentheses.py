# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.
#     Every close bracket has a corresponding open bracket of the same type.

class Solution:
    def isValid(self, s: str) -> bool:
        bracketStack = []
        for char in s:
            last = None if len(bracketStack) == 0 else bracketStack[-1]
            match char:
                case ')':
                    if last == '(': bracketStack.pop()
                    elif last == '{' or last == '[':
                        return False
                    else: bracketStack.append(char)
                case '}':
                    if last == '{': bracketStack.pop()
                    elif last == '(' or last == '[':
                        return False
                    else: bracketStack.append(char)
                case ']':
                    if last == '[': bracketStack.pop()
                    elif last == '{' or last == '(':
                        return False
                    else: bracketStack.append(char)
                case _:
                    bracketStack.append(char)
        return len(bracketStack) == 0