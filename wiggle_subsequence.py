# A wiggle sequence is a sequence where the differences between successive numbers strictly alternate between positive and negative. 
# The first difference (if one exists) may be either positive or negative. 
# A sequence with one element and a sequence with two non-equal elements are trivially wiggle sequences.

#     For example, [1, 7, 4, 9, 2, 5] is a wiggle sequence because the differences (6, -3, 5, -7, 3) alternate between positive 
#     and negative.
#     In contrast, [1, 4, 7, 2, 5] and [1, 7, 4, 5, 5] are not wiggle sequences. 
#     The first is not because its first two differences are positive, and the second is not because its last difference is zero.

# A subsequence is obtained by deleting some elements (possibly zero) from the original sequence, 
# leaving the remaining elements in their original order.

# Given an integer array nums, return the length of the longest wiggle subsequence of nums.

class Solution:
    def wiggleMaxLength(self, nums: list[int]) -> int:
        diffArray = [0 for i in range(len(nums) - 1)]
        for i in range(len(nums) - 1):
            diffArray[i] = nums[i+1] - nums[i]
        
        numSegments = 0
        increasing = None
        for i in range(len(diffArray)):
            if diffArray[i] == 0:
                continue
            elif increasing == None:
                increasing = diffArray[i] > 0
                numSegments += 1
            else:
                if diffArray[i] < 0:
                    if increasing:
                        numSegments += 1
                    increasing = False
                elif diffArray[i] > 0:
                    if not increasing:
                        numSegments += 1
                    increasing = True
        
        return numSegments + 1