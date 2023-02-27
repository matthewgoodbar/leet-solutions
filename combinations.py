# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

# You may return the answer in any order.

class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        if not n: return []
        if k == 1: return [[i] for i in range(1, n+1)]
        res = []
        for i in range(n, 0, -1):
            choices = [subChoices + [i] for subChoices in self.combine(i-1, k-1)]
            res = res + choices
        return res