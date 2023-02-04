# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), 
# ans[i] is the number of 1's in the binary representation of i.

class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for num in range(n+1):
            binString = format(num, "b")
            ones = 0
            for digit in binString:
                if digit == "1": ones += 1
            res.append(ones)
        return res