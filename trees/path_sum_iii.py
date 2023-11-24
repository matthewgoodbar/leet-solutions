# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        
        def trackSum(node, prevSums, target) -> int:

            count = 0
            newSums = [node.val + el for el in prevSums] + [node.val]
            for el in newSums:
                if el == target:
                    count += 1
            
            if node.left:
                count += trackSum(node.left, newSums, target)
            if node.right:
                count += trackSum(node.right, newSums, target)
            
            return count
        
        if not root:
            return 0
        
        return trackSum(root, [], targetSum)