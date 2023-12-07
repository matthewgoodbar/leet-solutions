from collections import deque

class StockSpanner:

    def __init__(self):
        #monotonically decreasing
        self.monostack = deque()
        self.day = 0

    def next(self, price: int) -> int:
        res = 1
        while self.monostack and self.monostack[-1][0] <= price:
          last = self.monostack.pop()
          res += last[1]
        self.monostack.append((price, res))
        print(self.monostack)
        return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

prices = [100,80,60,70,60,75,85]
s = StockSpanner()
print([s.next(price) for price in prices])