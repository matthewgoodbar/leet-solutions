class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> list[int]:

        if k == 0:
            return [int(str(i)*n) for i in range(1,10)]
        
        def buildNumbers(prev):
            res = []
            prevDigit = prev % 10
            plusK = prevDigit + k
            minusK = prevDigit - k
            if plusK < 10:
                withPlusK = (prev * 10) + plusK
                if len(str(withPlusK)) < n:
                    plusKRec = buildNumbers(withPlusK)
                    res = res + plusKRec
                else:
                    res.append(withPlusK)
            if minusK >= 0:
                withMinusK = (prev * 10) + minusK
                if len(str(withMinusK)) < n:
                    minusKRec = buildNumbers(withMinusK)
                    res = res + minusKRec
                else:
                    res.append(withMinusK)
            return res
        
        res = []
        for i in range(1,10):
            res = res + buildNumbers(i)
        return res