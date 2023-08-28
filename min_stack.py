class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minStack) == 0:
            self.minStack.append(val)
        else:
            lastMinVal = self.minStack[-1]
            if val < lastMinVal:
                self.minStack.append(val)
            else:
                self.minStack.append(lastMinVal)
        return None
        

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        return None
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]