from collections import deque

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: ListNode) -> int:
        
        stack = deque()
        pointer = head
        while pointer:
            stack.append(pointer.val)
            pointer = pointer.next
        
        maxSum = 0
        while stack:
            current = stack.popleft() + stack.pop()
            maxSum = max(maxSum, current)
        return maxSum