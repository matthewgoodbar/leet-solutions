# Given the root of a binary tree, return all duplicate subtrees.

# For each kind of duplicate subtrees, you only need to return the root node of any one of them.

# Two trees are duplicate if they have the same structure with the same node values.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> list[Optional[TreeNode]]:

        treeDict = {}
        res = set()

        def catalogueTrees(root: TreeNode) -> str:
            if not root: return ''
            leftKey = catalogueTrees(root.left) + 'l' if root.left else ''
            rightKey = catalogueTrees(root.right) + 'r' if root.right else ''
            treeKey = str(hash(str(root.val) + leftKey + rightKey))
            checkDict(root, treeKey)
            return treeKey
        
        def checkDict(root: TreeNode, key: str):
            if key not in treeDict:
                treeDict[key] = root
            else:
                res.add(treeDict[key])
        
        catalogueTrees(root)
        return res