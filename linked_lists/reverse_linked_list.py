# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prv = None
        cur = head
        if not head:
            return None
        nxt = head.next
        while cur:
            cur.next = prv
            prv = cur
            cur = nxt
            if nxt:
                nxt = nxt.next
        head = prv
        return head