class Solution:
    def maxProduct(self, nums: list[int]) -> int:

        currentMaxProd = None
        prods = []
        prevWasNegative = False
        for num in nums:

            if num == 0:
                if currentMaxProd == None:
                    currentMaxProd = 0
                if prods:
                    currentMaxProd = max(currentMaxProd, max(prods))
                prods = []
                continue

            if not prods:
                prods.append(num)
                if num < 0:
                    prevWasNegative = True
                continue
            
            if num < 0:
                if currentMaxProd != None:
                    currentMaxProd = max(currentMaxProd, max(prods))
                else:
                    currentMaxProd = max(prods)

            for i in range(len(prods)):
                prods[i] = prods[i] * num
            
            if prevWasNegative:
                prods.append(num)
            
            prevWasNegative = num < 0
        

        if prods:
            if currentMaxProd != None:
                return max(currentMaxProd, max(prods))
            else:
                return max(prods)
        else:
            return currentMaxProd

sol = Solution()
nums = [2,3]
print(sol.maxProduct(nums))