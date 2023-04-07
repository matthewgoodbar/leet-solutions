# You are a professional robber planning to rob houses along a street. 
# Each house has a certain amount of money stashed, 
# the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected 
# and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, 
# return the maximum amount of money you can rob tonight without alerting the police.

class Solution:
    def rob(self, nums: list[int]) -> int:

        memo = {}

        def robFromIdx(startIdx):
            if startIdx in memo:
                return memo[startIdx]
            houses = nums[startIdx:]
            if not houses:
                return 0
            if len(houses) == 1:
                return houses[0]
            if len(houses) == 2:
                return max(houses)
            if len(houses) == 3:
                return max(houses[0] + houses[2], houses[1])
            
            maxFromHere = max(robFromIdx(startIdx+2), robFromIdx(startIdx+3))
            memo[startIdx] = houses[0] + maxFromHere
            return memo[startIdx]
        
        return max(robFromIdx(i) for i in range(len(nums)))