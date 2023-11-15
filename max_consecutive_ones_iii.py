class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        
        #start from the beginning, fill 0 spaces with 1's as long as we have k's
        #if we run out of k's, march up the start point until we find a k to reuse

        currentKs = k
        start = end = 0
        maxOnes = currentCount = 0
        while end < len(nums):
            if nums[end] == 0:
                #if our end is 0, we can't advance until we get a k to pave the way
                if k == 0: 
                    #with k = 0, just advance start and end until we find a 1
                    end += 1
                    start = end
                    currentCount = 0
                elif currentKs > 0: 
                    #we have a k to spare, fill 0 with 1 and advance end
                    currentKs -= 1
                    end += 1
                    currentCount += 1
                else: 
                    #we don't have a spare k, advance the start until we pick up a 1 we placed
                    if nums[start] == 0:
                        currentKs += 1
                    start += 1
                    currentCount -= 1
            else:
                #end is 1, safe to advance
                currentCount += 1
                end += 1
            #scrutinize our current 1 count
            if currentCount > maxOnes:
                maxOnes = currentCount
        
        return maxOnes

sol = Solution()
arr = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(sol.longestOnes(arr, k))