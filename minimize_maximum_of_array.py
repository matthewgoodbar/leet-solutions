class Solution:
    def minimizeArrayValue(self, nums: list[int]) -> int:
        changed = True
        while changed:
            print(nums)
            changed = False
            for i in range(len(nums) - 1, -1, -1):
                if i == 0:
                    continue
                if nums[i] - nums[i-1] > 0:
                    nums[i] -= 1
                    nums[i-1] += 1
                    changed = True
        return max(nums)

nums = [6,9,3,8,14]
sol = Solution()
sol.minimizeArrayValue(nums)