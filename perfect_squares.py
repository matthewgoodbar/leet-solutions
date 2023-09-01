class Solution:
    def numSquares(self, n: int) -> int:

        memo = {}

        def numSquaresRec(n):
            if n in memo:
                return memo[n]
            
            if n < 4:
                memo[n] = n
                return n

            if n ** 0.5 == int(n ** 0.5):
                memo[n] = 1
                return 1

            psLessThanN = [i*i for i in range(1,int(n**0.5)+1)]

            combos = []
            for ps in psLessThanN[::-1]:
                combos.append(numSquaresRec(n - ps))
            
            memo[n] = 1 + min(combos)
            return memo[n]

        return numSquaresRec(n)

sol = Solution()
print(sol.numSquares(55))