# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:

        pointer = root
        pointerParent = None

        while pointer and pointer.val != key:
            pointerParent = pointer
            if key < pointer.val:
                pointer = pointer.left
            else:
                pointer = pointer.right
        
        if pointer is None:
            return root
        
        if pointer.left and pointer.right:
            #find successor, recursively delete, replace pointer val with successor val
            successor = pointer.right
            while successor.left:
                successor = successor.left
            pointer.right = self.deleteNode(pointer.right, successor.val)
            pointer.val = successor.val
        elif pointer.left or pointer.right:
            #key only has one child
            if pointerParent:
                #root is not key
                if pointerParent.left is pointer:
                    pointerParent.left = pointer.left or pointer.right
                else:
                    pointerParent.right = pointer.left or pointer.right
            else:
                #root is key
                return pointer.left or pointer.right
        else:
            #key has no children
            if pointerParent:
                #root is not key
                if pointerParent.left is pointer:
                    pointerParent.left = None
                else:
                    pointerParent.right = None
            else:
                #root is key
                return None
        
        return root