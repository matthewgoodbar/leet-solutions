# You are given an integer array nums with no duplicates. 
# A maximum binary tree can be built recursively from nums using the following algorithm:

#     Create a root node whose value is the maximum value in nums.
#     Recursively build the left subtree on the subarray prefix to the left of the maximum value.
#     Recursively build the right subtree on the subarray suffix to the right of the maximum value.

# Return the maximum binary tree built from nums.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums: list[int]) -> Optional[TreeNode]:
        if len(nums) == 0: return None
        if len(nums) == 1: return TreeNode(nums[0])
        maxIdx = 0
        maxNum = 0
        for idx, num in enumerate(nums):
            if num > maxNum: maxNum, maxIdx = num, idx
        root = TreeNode(maxNum)
        root.left = self.constructMaximumBinaryTree(nums[:maxIdx])
        root.right = self.constructMaximumBinaryTree(nums[maxIdx+1:])
        return root