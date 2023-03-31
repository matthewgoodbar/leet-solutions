# Given the head of a linked list and a value x, 
# partition it such that all nodes less than x come before nodes greater than or equal to x.

# You should preserve the original relative order of the nodes in each of the two partitions.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head: return None
        ltHead = gteHead = ltTail = gteTail = None
        while head:
            if head.val >= x:
                if not gteHead:
                    gteHead = gteTail = head
                else:
                    gteTail.next = head
                    gteTail = gteTail.next
                head = head.next
                gteTail.next = None
            else:
                if not ltHead:
                    ltHead = ltTail = head
                else:
                    ltTail.next = head
                    ltTail = ltTail.next
                head = head.next
                ltTail.next = None
        if ltHead:
            ltTail.next = gteHead
            return ltHead
        else:
            return gteHead