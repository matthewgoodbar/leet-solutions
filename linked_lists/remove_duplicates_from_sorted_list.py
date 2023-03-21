# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. 
# Return the linked list sorted as well.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        prev = head
        seen = {prev.val}
        current = prev.next
        while current:
            if current.val in seen:
                prev.next = current.next
                current = prev.next
            else:
                seen.add(current.val)
                prev = current
                current = current.next
        return head