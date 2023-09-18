# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sortedHead = head
        head = head.next
        sortedHead.next = None

        while head:
            temp = head
            head = head.next
            temp.next = None
            sortedPointer = sortedHead
            sortedPrev = None
            placed = False
            while sortedPointer:
                if temp.val <= sortedPointer.val:
                    if sortedPointer == sortedHead:
                        temp.next = sortedPointer
                        sortedHead = temp
                        placed = True
                        break
                    else:
                        sortedPrev.next = temp
                        temp.next = sortedPointer
                        placed = True
                        break
                sortedPrev = sortedPointer
                sortedPointer = sortedPointer.next
            if not placed:
                sortedPrev.next = temp
        
        return sortedHead