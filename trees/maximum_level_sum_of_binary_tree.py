from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        queue = deque()
        levelSums = {}
        queue.append((root, 1))
        while queue:
            node, level = queue.popleft()
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
            
            if level in levelSums:
                levelSums[level] += node.val
            else:
                levelSums[level] = node.val
        
        maxLevel = 1
        currentMax = levelSums[1]
        for level in levelSums:
            if levelSums[level] > currentMax:
                currentMax = levelSums[level]
                maxLevel = level
        return maxLevel