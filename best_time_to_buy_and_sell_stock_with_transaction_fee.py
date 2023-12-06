class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        
        n = len(prices)
        dpBuy = [0 for _ in range(n)]
        dpSell = [0 for _ in range(n)]
        dpBuy[0] -= prices[0]

        for i in range(1,n):
            dpBuy[i] = max(dpBuy[i-1], dpSell[i-1] - prices[i])
            dpSell[i] = max(dpSell[i-1], dpBuy[i-1] + prices[i] - fee)
        
        return dpSell[-1]