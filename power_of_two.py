# Given an integer n, return true if it is a power of two. Otherwise, return false.

# An integer n is a power of two, if there exists an integer x such that n == 2x.

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 0:
            return False
        binary = bin(n).split('b')[1]
        ones = 0
        for char in binary:
            if char == '1':
                ones += 1
        return ones == 1