import random

class Solution:

    def __init__(self, nums: list[int]):
        self.original = nums
        self.shuffled = [num for num in nums]

    def reset(self) -> list[int]:
        self.shuffled = [num for num in self.original]
        return self.shuffled

    def shuffle(self) -> list[int]:
        random.shuffle(self.shuffled)
        return self.shuffled


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()