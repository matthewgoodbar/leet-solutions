class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        oneEnd = float('inf')
        twoEnd = float('inf')
        for num in nums:
            if num <= oneEnd:
                oneEnd = num
            elif num <= twoEnd:
                twoEnd = num
            else:
                return True
        return False

arr = [4,5,1,2]
sol = Solution()
print(sol.increasingTriplet(arr))