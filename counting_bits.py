class Solution:
    def countBits(self, n: int) -> list[int]:
        res = []
        for i in range(n+1):
            if i == 0:
                res.append(0)
            elif i == 1:
                res.append(1)
            elif i % 2 == 0:
                res.append(res[i//2])
            else:
                res.append(res[i//2]+1)
        return res