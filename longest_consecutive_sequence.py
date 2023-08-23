class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        groups = {}
        maxLen = 0
        for num in nums:
            if num not in groups:
                groupLen = 0
                if num+1 not in groups and num-1 not in groups:
                    groups[num] = num
                    groupLen = 1
                elif num+1 in groups and num-1 in groups:
                    #num can bridge a gap
                    if groups[num-1] == "NOT A BOUND" or groups[num+1] == "NOT A BOUND":
                        next
                    lowerGroupUpperBound = num-1
                    upperGroupLowerBound = num+1
                    lowerGroupLowerBound = groups[lowerGroupUpperBound]
                    upperGroupUpperBound = groups[upperGroupLowerBound]
                    if lowerGroupLowerBound != lowerGroupUpperBound:
                        groups[lowerGroupUpperBound] = "NOT A BOUND"
                    if upperGroupLowerBound != upperGroupUpperBound:
                        groups[upperGroupLowerBound] = "NOT A BOUND"
                    groups[upperGroupUpperBound] = lowerGroupLowerBound
                    groups[lowerGroupLowerBound] = upperGroupUpperBound
                    groups[num] = "NOT A BOUND"
                    groupLen = upperGroupUpperBound - lowerGroupLowerBound + 1
                elif num-1 in groups:
                    #num is the upper bound of a group
                    if groups[num-1] == "NOT A BOUND":
                        next
                    lowerGroupUpperBound = num-1
                    lowerGroupLowerBound = groups[lowerGroupUpperBound]
                    if lowerGroupLowerBound != lowerGroupUpperBound:
                        groups[lowerGroupUpperBound] = "NOT A BOUND"
                    groups[num] = lowerGroupLowerBound
                    groups[lowerGroupLowerBound] = num
                    groupLen = num - lowerGroupLowerBound + 1
                elif num+1 in groups:
                    #num is the lower bound of a group
                    if groups[num+1] == "NOT A BOUND":
                        next
                    upperGroupLowerBound = num+1
                    upperGroupUpperBound = groups[upperGroupLowerBound]
                    if upperGroupLowerBound != upperGroupUpperBound:
                        groups[upperGroupLowerBound] = "NOT A BOUND"
                    groups[num] = upperGroupUpperBound
                    groups[upperGroupUpperBound] = num
                    groupLen = upperGroupUpperBound - num + 1
                if groupLen > maxLen:
                    maxLen = groupLen
        
        return maxLen

sol = Solution()
# nums = [100,4,200,1,3,2]
nums = [0,3,7,2,5,8,4,6,0,1]
print(sol.longestConsecutive(nums))