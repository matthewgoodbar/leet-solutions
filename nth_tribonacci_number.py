class Solution:
    def tribonacci(self, n: int) -> int:
        
        cache = {0:0, 1:1, 2:1}

        def tribRec(n):
            if n in cache:
                return cache[n]
            res = tribRec(n-1) + tribRec(n-2) + tribRec(n-3)
            cache[n] = res
            return res
        
        return tribRec(n)