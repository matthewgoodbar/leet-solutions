# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def findGoodNodes(node, prevLargest) -> int:
            if node.val >= prevLargest:
                goodCount = 1
            else:
                goodCount = 0
            
            if node.left:
                goodCount += findGoodNodes(node.left, max(node.val, prevLargest))
            if node.right:
                goodCount += findGoodNodes(node.right, max(node.val, prevLargest))
            
            return goodCount
        
        return findGoodNodes(root, root.val)