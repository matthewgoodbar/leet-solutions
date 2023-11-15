class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 0
        start = 0
        end = 1
        zeros = 0
        if nums[0] == 0:
            zeros += 1
        
        while end < len(nums):
            if zeros == 0: #we're allowed 1 zero
                if nums[end] == 0:
                    zeros += 1
                end += 1
            elif zeros > 1 or nums[end] == 0: #advance start and end
                if nums[start] == 0:
                    zeros -= 1
                start += 1
                if nums[end] == 0:
                    zeros += 1
                end += 1
            else: #advance end
                end += 1
            print(f'start: {start}, end: {end}, zeros: {zeros}')
        
        return end - start - 1

sol = Solution()
arr = [0,1,1,1,0,1,1,0,1]
print(sol.longestSubarray(arr))