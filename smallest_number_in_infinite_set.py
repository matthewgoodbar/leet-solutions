import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.infinite = 1
        self.heap = []
        self.heapSet = set()

    def popSmallest(self) -> int:
        if self.heap:
            res = heapq.heappop(self.heap)
            self.heapSet.remove(res)
            return res
        else:
            self.infinite += 1
            return self.infinite-1

    def addBack(self, num: int) -> None:
        if num >= self.infinite:
            return None
        if num not in self.heapSet:
            heapq.heappush(self.heap, num)
            self.heapSet.add(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)