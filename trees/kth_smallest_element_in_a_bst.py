# Given the root of a binary search tree, and an integer k, 
# return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.res = 0
        self.traverse(root)
        return self.res
    
    def traverse(self, node):
        if not node: return
        self.traverse(node.left)
        self.k -= 1
        if self.k == 0: self.res = node.val
        self.traverse(node.right)