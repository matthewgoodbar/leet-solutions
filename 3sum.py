# Given an integer array nums, 
# return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = set()

        def twoSum(nums: list[int], start: int, target: int):
            if len(nums) - start < 2:
                return []
            pairs = []
            record = {}
            for j in range(start, len(nums) - 1):
                if target - nums[j] not in record:
                    record[target - nums[j]] = j
            for k in range(start + 1, len(nums)):
                if nums[k] in record and record[nums[k]] < k:
                    pairs.append([record[nums[k]], k])
            print(record)
            return pairs


        for i in range(len(nums) - 2):
            pairsToI = twoSum(nums, i + 1, nums[i] * -1)
            if pairsToI:
                for pair in pairsToI:
                    triplet = [nums[i], nums[pair[0]], nums[pair[1]]]
                    res.add(tuple(sorted(triplet)))
        
        return res
    
nums = [-2,0,1,1,2]
sol = Solution()
sol.threeSum(nums)