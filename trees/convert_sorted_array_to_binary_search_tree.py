
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: list[int]):

        def treeByChunk(arr: list[int]):
            if len(arr) == 0:
                return None
            if len(arr) == 1:
                return TreeNode(val = arr[0])
            medianIdx = len(arr) // 2
            root = TreeNode(val = arr[medianIdx])
            root.left = treeByChunk(arr[:medianIdx])
            root.right = treeByChunk(arr[medianIdx+1:])
            return root
        
        return treeByChunk(nums)

nums = [-10,-3,0,5,9]
sol = Solution()
sol.sortedArrayToBST(nums)