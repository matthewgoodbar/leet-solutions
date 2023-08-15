# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        #Base cases
        if not head or not head.next:
            return head
        if k == 1:
            return head
        
        #Reverse a single group given head and tail, returns new head and tail
        def reverseGroup(head, tail):
            tail.next = None
            if head.next == tail:
                tail.next = head
                head.next = None
            else:
                first = head
                second = first.next
                third = second.next
                first.next = None
                while third:
                    second.next = first
                    first = second
                    second = third
                    third = third.next
                second.next = first
            head, tail = tail, head
            return [head, tail]
        
        #each [head, tail] pair in groups is a portion of the list k elements long
        #extraHead is the head of the remaining n % k elements
        groups = []
        grpStart = head
        grpEnd = head
        grpSize = 1
        extraHead = None
        while grpEnd:
            grpEnd = grpEnd.next
            if grpEnd:
                grpSize += 1
                if grpSize == k:
                    groups.append([grpStart, grpEnd])
                    grpStart = grpEnd = grpEnd.next
                    grpSize = 1
        if grpStart and not grpEnd:
            extraHead = grpStart
        
        #reverse each group
        newGroups = []
        for group in groups:
            newRefs = reverseGroup(group[0], group[1])
            newGroups.append(newRefs)
        
        #link each group, and extra head if exists
        for i in range(len(newGroups)-1):
            firstTail = newGroups[i][1]
            secondHead = newGroups[i+1][0]
            firstTail.next = secondHead
        
        if extraHead:
            lastGroupTail = newGroups[-1][1]
            lastGroupTail.next = extraHead

        return newGroups[0][0]