# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        digitSum = 0
        carryOver = 0
        head = current = ListNode()
        firstPass = True
        while l1 or l2:
            if not firstPass:
                current.next = ListNode()
                current = current.next
            firstPass = False
            digitSum = carryOver
            if l1: digitSum += l1.val
            if l2: digitSum += l2.val
            if digitSum > 9:
                carryOver = digitSum // 10
                digitSum = digitSum % 10
            else:
                carryOver = 0
            current.val = digitSum
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        if carryOver > 0:
            current.next = ListNode(carryOver)
        return head