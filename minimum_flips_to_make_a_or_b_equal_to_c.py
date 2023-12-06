class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        count = 0
        while (a + b + c) > 0:
            if c % 2 == 0:
                # c is even, we want a 0 in the first bit
                if a % 2 == 1 and b % 2 == 1:
                    count += 2
                elif a % 2 == 1 or b % 2 == 1:
                    count += 1
            else:
                # c is odd, we want a 1 in the first bit
                if a % 2 == 0 and b % 2 == 0:
                    count += 1
            a >>= 1
            b >>= 1
            c >>= 1
        return count