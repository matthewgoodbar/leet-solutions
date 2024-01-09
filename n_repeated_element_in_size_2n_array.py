class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        n = len(nums) // 2
        h = {}
        for num in nums:
            if num in h:
                h[num] += 1
            else:
                h[num] = 1
            if h[num] == n:
                return num