# Given an integer n, return the number of trailing zeroes in n!.

# Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0:
            return 0
        else:
            return n // 5 + self.trailingZeroes(n // 5)