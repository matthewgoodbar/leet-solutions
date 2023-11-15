class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        maxHeight = currentHeight = 0
        for delta in gain:
            currentHeight += delta
            maxHeight = max(maxHeight, currentHeight)
        return maxHeight