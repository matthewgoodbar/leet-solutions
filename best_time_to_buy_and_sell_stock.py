# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = 0
        currentMaxProfit = 0
        for idx, currentPrice in enumerate(prices):
            if idx == 0: continue
            if currentPrice - prices[start] > currentMaxProfit:
                currentMaxProfit = currentPrice - prices[start]
            if currentPrice < prices[start]:
                start = idx
        return currentMaxProfit