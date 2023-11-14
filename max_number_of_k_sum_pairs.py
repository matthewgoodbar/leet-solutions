class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        unpaired = {}
        count = 0
        for num in nums:
            if k - num in unpaired:
                if unpaired[k-num] == 1:
                    del unpaired[k-num]
                else:
                    unpaired[k-num] -= 1
                count += 1
            elif num in unpaired:
                unpaired[num] += 1
            else:
                unpaired[num] = 1
        return count