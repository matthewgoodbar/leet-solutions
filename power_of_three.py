import math

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        error = 1e-10
        exp = math.log(n, 3)
        return abs(round(exp) - exp) < error