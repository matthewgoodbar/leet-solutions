# Given a singly linked list, return a random node's value from the linked list. 
# Each node must have the same probability of being chosen.

# Implement the Solution class:

#     Solution(ListNode head) Initializes the object with the head of the singly-linked list head.
#     int getRandom() Chooses a node randomly from the list and returns its value. 
#     All the nodes of the list should be equally likely to be chosen.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
import random
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.length = 0
        pointer = head
        while pointer:
            self.length += 1
            pointer = pointer.next
        

    def getRandom(self) -> int:
        num = random.randint(1,self.length)
        pointer = self.head
        while num > 1:
            pointer = pointer.next
            num -= 1
        return pointer.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()