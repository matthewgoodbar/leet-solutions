# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        if not root:
            return 0

        def findLongest(node, previousWasLeft, count) -> int:

            if not node:
                return count

            if previousWasLeft:
                return max(findLongest(node.left, True, 0), findLongest(node.right, False, count+1))
            else:
                return max(findLongest(node.left, True, count+1), findLongest(node.right, False, 0))
        
        return max(findLongest(root.left, True, 0), findLongest(root.right, False, 0))