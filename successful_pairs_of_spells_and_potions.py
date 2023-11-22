import math

class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:

        pairs = []
        potions.sort()

        def binSearch(arr, k):

            high = len(arr)
            low = 0
            mid = high // 2

            while True:
                if arr[mid] >= k:
                    if mid == 0:
                        return 0
                    elif arr[mid-1] < k:
                        return mid
                    else:
                        high = mid
                        mid = (low + high) // 2
                else:
                    if mid == len(arr)-1:
                        return -1
                    else:
                        low = mid
                        mid = (low + high) // 2

        for spell in spells:
            desiredStr = math.ceil(success / spell)
            cutoffIdx = binSearch(potions, desiredStr)
            if cutoffIdx == -1:
                pairs.append(0)
            else:
                pairs.append(len(potions) - cutoffIdx)
        
        return pairs