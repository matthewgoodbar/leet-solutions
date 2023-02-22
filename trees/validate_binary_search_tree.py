# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

#     The left
#     subtree
#     of a node contains only nodes with keys less than the node's key.
#     The right subtree of a node contains only nodes with keys greater than the node's key.
#     Both the left and right subtrees must also be binary search trees.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return False
        if (not root.left) and (not root.right): return True

        def maxVal(root) -> int:
            if not root: return None
            currentMax = root.val
            if root.left:
                leftMax = maxVal(root.left)
                currentMax = max(leftMax, currentMax)
            if root.right:
                rightMax = maxVal(root.right)
                currentMax = max(rightMax, currentMax)
            return currentMax
        
        def minVal(root) -> int:
            if not root: return None
            currentMin = root.val
            if root.left:
                leftMin = minVal(root.left)
                currentMin = min(leftMin, currentMin)
            if root.right:
                rightMin = minVal(root.right)
                currentMin = min(rightMin, currentMin)
            return currentMin
        
        if root.left:
            if root.val <= maxVal(root.left) or (not self.isValidBST(root.left)):
                return False
        if root.right:
            if root.val >= minVal(root.right) or (not self.isValidBST(root.right)):
                return False
        return True