# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. 
# You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. 
# Two combinations are unique if the frequency of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        if target <= 1: return []
        res = []
        for can in candidates:
            if can == target: res.append([can])
            if can < target:
                subCandidates = self.combinationSum(candidates, target-can)
                for subCan in subCandidates:
                    subCan.append(can)
                    subCan.sort()
                    if subCan not in res: res.append(subCan)
        return res