class Solution:
    def jump(self, nums: list[int]) -> int:

        if len(nums) == 1:
            return 0
        
        n = 1
        currentSet = {len(nums)-1}
        currentMindex = len(nums)-1
        
        while 0 not in currentSet:
            newSet = set()
            newMindex = currentMindex
            for i in range(currentMindex):
                if i not in currentSet:
                    possibleJumps = [i + j for j in range(1,nums[i]+1)]
                    for jump in possibleJumps:
                        if jump in currentSet:
                            newSet.add(i)
                            if i < newMindex:
                                newMindex = i
            if 0 in newSet:
                return n
            else:
                n += 1
                currentSet = newSet
                currentMindex = newMindex

sol = Solution()
nums = [2,3,1,1,4]
print(sol.jump(nums))