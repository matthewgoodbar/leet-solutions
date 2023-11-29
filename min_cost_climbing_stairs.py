class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        
        dp = [0 for _ in range(len(cost))]
        dp[0] = cost[0]
        dp[1] = cost[1]

        #dp[i] = minimum cost to jump from position i
        for i in range(2, len(dp)):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        
        #minimum total cost will be the minimum between the last two costs in dp
        return min(dp[-1],dp[-2])