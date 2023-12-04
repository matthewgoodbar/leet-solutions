# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: ListNode) -> int:
        
        n = 0
        nums = {}
        pointer = head
        while pointer:
            nums[n] = pointer.val
            n += 1
            pointer = pointer.next
        
        maxSum = 0
        for i in range(n//2):
            current = nums[i] + nums[n-i-1]
            maxSum = max(maxSum, current)
        return maxSum