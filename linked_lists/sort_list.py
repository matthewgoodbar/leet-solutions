# Given the head of a linked list, return the list after sorting it in ascending order.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        listLength = 0
        pointer = head
        while pointer:
            listLength += 1
            pointer = pointer.next
        
        def mergeSort(head, length):
            if length <= 1:
                return head
            mid = length // 2
            midIdx = 0
            leftTail = head
            while midIdx < mid - 1:
                leftTail = leftTail.next
                midIdx += 1
            rightHead = leftTail.next
            leftTail.next = None
            leftHead = mergeSort(head, mid)
            rightHead = mergeSort(rightHead, mid if length % 2 == 0 else mid + 1)
            return merge(leftHead, rightHead)
        
        def merge(leftList, rightList):
            head = tail = None
            while leftList and rightList:
                if leftList.val <= rightList.val:
                    if head:
                        tail.next = leftList
                        leftList = leftList.next
                        tail = tail.next
                        tail.next = None
                    else:
                        head = tail = leftList
                        leftList = leftList.next
                        tail.next = None
                else:
                    if head:
                        tail.next = rightList
                        rightList = rightList.next
                        tail = tail.next
                        tail.next = None
                    else:
                        head = tail = rightList
                        rightList = rightList.next
                        tail.next = None
            if not leftList:
                tail.next = rightList
            else:
                tail.next = leftList
            return head
        
        return mergeSort(head, listLength)