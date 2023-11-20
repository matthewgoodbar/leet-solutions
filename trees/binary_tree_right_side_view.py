from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> list[int]:
        if root is None:
            return []
        queue = deque()
        queue.append((root, 1))
        res = []
        prev = None
        while queue:
            node, level = queue.popleft()
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
            if prev and prev[1] != level:
                res.append(prev[0].val)
            prev = (node, level)
        res.append(prev[0].val)
        return res