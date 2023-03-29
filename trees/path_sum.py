# Given the root of a binary tree and an integer targetSum, 
# return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

# A leaf is a node with no children.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False
        if (not root.right) and (not root.left):
            return True if targetSum == root.val else False
        
        if root.right:
            if self.hasPathSum(root.right, targetSum - root.val): return True

        if root.left:
            if self.hasPathSum(root.left, targetSum - root.val): return True
        
        return False