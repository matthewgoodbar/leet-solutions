# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, n * -1)
        if n % 2 == 0:
            half = self.myPow(x, n//2)
            return half * half
        else:
            return x * self.myPow(x, n-1)