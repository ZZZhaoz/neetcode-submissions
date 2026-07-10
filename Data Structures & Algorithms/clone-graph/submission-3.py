"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        newnode = Node(node.val)
        new = {}
        new[node] = newnode

        q = collections.deque()
        q.append(node)
        while q:
            no = q.popleft()        
            for neighbor in no.neighbors:
                if neighbor not in new:
                    new[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                new[no].neighbors.append(new[neighbor])
        return new[node]