# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

# Implement the LRUCache class:

#     LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
#     int get(int key) Return the value of the key if the key exists, otherwise return -1.
#     void put(int key, int value) Update the value of the key if the key exists. 
#     Otherwise, add the key-value pair to the cache. 
#     If the number of keys exceeds the capacity from this operation, evict the least recently used key.

# The functions get and put must each run in O(1) average time complexity.

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.dll = self.DoubleLinkList()
        self.cap = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.dll.update(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.dll.update(node)
        else:
            if self.dll.size == self.cap: 
                removedKey = self.dll.remove()
                del self.cache[removedKey]
            node = self.dll.add(value, key)
            self.cache[key] = node
    
    class DoubleLinkList:

        def __init__(self):
            self.head = None
            self.tail = None
            self.size = 0
        
        def add(self, val, key):
            if self.size is 0:
                self.head = self.Node(val, key)
                self.tail = self.head
                self.size += 1
                return self.head
            else:
                new = self.Node(val, key)
                self.head.next = new
                new.prev = self.head
                self.head = new
                self.size += 1
                return new
        
        def update(self, node):
            if not node.next:
                return node
            if not node.prev:
                self.tail = self.tail.next
            prevNode = node.prev
            nextNode = node.next
            if prevNode: prevNode.next = nextNode
            if nextNode: nextNode.prev = prevNode
            self.head.next = node
            node.prev = self.head
            node.next = None
            self.head = node
            return node
        
        def remove(self):
            if self.size is 0: return
            if self.size is 1:
                key = self.head.key
                self.head = None
                self.tail = None
                self.size -= 1
                return key
            key = self.tail.key
            nextNode = self.tail.next
            nextNode.prev = None
            self.tail = nextNode
            self.size -= 1
            return key

        class Node:

            def __init__(self, val = None, key = None):
                self.val = val
                self.key = key
                self.next = None
                self.prev = None

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)