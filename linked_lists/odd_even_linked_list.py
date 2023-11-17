# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        evenHead = even = head
        if evenHead:
            oddHead = odd = evenHead.next
        else:
            return None
        
        if not oddHead:
            return evenHead
        
        while even and odd:
            if even.next is odd:
                if odd.next:
                    even.next = odd.next
                    even = even.next
                else:
                    break
            else:
                odd.next = even.next
                odd = odd.next

        even.next = oddHead
        return evenHead