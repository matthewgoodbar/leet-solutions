class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:

        def twoSum(nums, target):
            if len(nums) < 2:
                return None
            res = []
            d = {}
            for i in range(len(nums)):
                if nums[i] not in d:
                    d[target - nums[i]] = i
                else:
                    res.append([d[nums[i]], i])
            return res if res else None
        
        def threeSum(nums, target):
            if len(nums) < 3:
                return None
            res = []
            for i in range(len(nums) - 2):
                twos = twoSum(nums[i+1:], target-nums[i])
                if twos:
                    for pair in twos:
                        res.append([i, pair[0]+i+1, pair[1]+i+1])
            return res if res else None
        
        res = []
        for i in range(len(nums)-3):
            threes = threeSum(nums[i+1:], target-nums[i])
            if threes:
                for triplet in threes:
                    quad = sorted([nums[i], nums[triplet[0]+i+1], nums[triplet[1]+i+1], nums[triplet[2]+i+1]])
                    if quad not in res:
                        res.append(quad)
        return res

# nums = [1,0,-1,0,-2,2]
nums = [2,2,2,2,2]
s = Solution()
print(s.fourSum(nums, 8))