# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        nodes = {}
        n = 0
        pointer = head
        while pointer:
            nodes[n] = pointer
            pointer = pointer.next
            nodes[n].next = None
            n += 1
        n -= 1

        first = 0
        last = n
        parity = True
        while first < last:
            if parity:
                node = nodes[first]
                node.next = nodes[last]
                first += 1
            else:
                node = nodes[last]
                node.next = nodes[first]
                last -= 1
            parity = not parity
        
        return None