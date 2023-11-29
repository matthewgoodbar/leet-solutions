class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        
        def getCombos(k, n, lowerBound):
            if k == 1:
                if n in range(lowerBound, 10):
                    return [[n]]
                else:
                    return []
            
            res = []
            for i in range(lowerBound, 10):
                subRes = getCombos(k-1, n-i, i+1)
                if subRes:
                    for combo in subRes:
                        res.append([i] + combo)
            return res

        return getCombos(k, n, 1)