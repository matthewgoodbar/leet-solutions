class Solution:
    def evalRPN(self, tokens: list[str]) -> int:

        stack = []
        operands = ["+","-","*","/"]

        def evaluate(a, b, operand):
            if operand == "+":
                return a + b
            if operand == "-":
                return a - b
            if operand == "*":
                return a * b
            if operand == "/":
                return int(a / b)
        
        for token in tokens:
            if token not in operands:
                stack.append(int(token))
            else:
                print(token)
                b = stack.pop()
                a = stack.pop()
                res = evaluate(a, b, token)
                stack.append(res)
            print(stack)
        
        return stack[0]

sol = Solution()
# tokens = ['10','6','9','3','+','-11','*','/','*','17','+','5','+']
tokens = ['4','-2','/','2','-3','-','-']
print(sol.evalRPN(tokens))