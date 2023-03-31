# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. 
# In how many distinct ways can you climb to the top?

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def climbStairsWithMemo(n):
            if n <= 2: return n
            if n in memo:
                return memo[n]
            else:
                res = climbStairsWithMemo(n-1) + climbStairsWithMemo(n-2)
                memo[n] = res
                return res
        
        return climbStairsWithMemo(n)