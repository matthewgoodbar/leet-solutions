# You are given an integer array height of length n. 
# There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

class Solution:
    def maxArea(self, height: list[int]) -> int:
        maxVol = min(height[0], height[-1]) * (len(height) - 1)
        while len(height) > 2:
            if height[0] < height[-1]:
                height.pop(0)
            else:
                height.pop()
            currentVol = min(height[0], height[-1]) * (len(height) - 1)
            if currentVol > maxVol: maxVol = currentVol
        return maxVol