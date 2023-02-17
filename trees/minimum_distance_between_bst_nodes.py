# Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        orderedList = []
        self.recordInOrder(root, orderedList)
        differenceList = []
        for idx, entry in enumerate(orderedList):
            if idx == 0: continue
            differenceList.append(abs(entry - orderedList[idx-1]))
        return min(differenceList)
    
    def recordInOrder(self, node: Optional[TreeNode], records: list) -> list:
        if not node: return
        self.recordInOrder(node.left, records)
        records.append(node.val)
        self.recordInOrder(node.right, records)