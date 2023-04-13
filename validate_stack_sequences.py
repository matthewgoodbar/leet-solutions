# Given two integer arrays pushed and popped each with distinct values, 
# return true if this could have been the result of a sequence of push and pop operations on an initially empty stack, 
# or false otherwise.

class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        stack = []
        for el in pushed:
            stack.append(el)
            while (stack and popped) and stack[-1] == popped[0]:
                stack.pop()
                popped.pop(0)
        
        return len(popped) == 0