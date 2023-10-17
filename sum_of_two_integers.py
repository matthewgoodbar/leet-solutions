import math

class Solution:
    def getSum(self, a: int, b: int) -> int:
        num = (2 ** a) * (2 ** b)
        return int(math.log(num, 2))