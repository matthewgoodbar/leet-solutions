class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        def simulateShipment(cap: int):
            daysUsed = 1
            currentLoad = 0
            for weight in weights:
                if currentLoad + weight > cap:
                    daysUsed += 1
                    currentLoad = weight
                else:
                    currentLoad += weight
            return daysUsed <= days
        minCap = max(weights)
        maxCap = sum(weights)
        while minCap < maxCap:
            midpoint = (minCap + maxCap) // 2
            if simulateShipment(midpoint):
                maxCap = midpoint
            else:
                minCap = midpoint + 1
        return maxCap



weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
sol = Solution()
print(sol.shipWithinDays(weights, days))