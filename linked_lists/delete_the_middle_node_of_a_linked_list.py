# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head.next:
            return None

        fast = slow1 = head
        slow2 = None
        index = 0
        advanceThisTime = True
        while fast.next:
            fast = fast.next
            if advanceThisTime:
                advanceThisTime = False
                if slow2 is None or slow2.next is slow1:
                    slow2 = slow1.next
                else:
                    slow1 = slow2.next
            else:
                advanceThisTime = True
        
        if slow1 is slow2.next:
            slow2.next = slow1.next
        else:
            slow1.next = slow2.next
        
        return head