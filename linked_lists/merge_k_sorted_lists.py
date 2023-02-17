# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        head = None
        current = None
        lists = list(filter(lambda node: node != None, lists))
        while len(lists) > 0:
            minIndex = lists.index(min(lists, key = lambda node: node.val))
            if not head: head = current = lists[minIndex]
            else:
                current.next = lists[minIndex]
                current = current.next
            if lists[minIndex].next:
                lists[minIndex] = lists[minIndex].next
            else:
                del lists[minIndex]
        return head