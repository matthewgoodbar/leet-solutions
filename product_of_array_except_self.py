class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefixArray = [1 for i in range(len(nums))]
        suffixArray = [1 for i in range(len(nums))]

        for i in range(1, len(prefixArray)):
            prefixArray[i] = prefixArray[i-1] * nums[i-1]
        
        for i in range(len(suffixArray)-2, -1, -1):
            suffixArray[i] = suffixArray[i+1] * nums[i+1]
        
        return [prefixArray[i] * suffixArray[i] for i in range(len(nums))]