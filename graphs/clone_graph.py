# Given a reference of a node in a connected undirected graph.

# Return a deep copy (clone) of the graph.

# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Node) -> Node:
        if not node: return None
        new = Node(node.val)
        seen = {node.val: new}
        queue = [node]
        while queue:
            current = queue.pop(0)
            clone = seen[current.val]
            for neighbor in current.neighbors:
                if neighbor.val not in seen:
                    seen[neighbor.val] = Node(neighbor.val)
                    queue.append(neighbor)
                clone.neighbors.append(seen[neighbor.val])
        
        return new