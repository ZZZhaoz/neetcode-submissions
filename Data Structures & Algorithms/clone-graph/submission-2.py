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
        nodemap = {}
        nodemap[node] = newnode

        q = collections.deque()
        q.append(node)
        while q:
            n = q.popleft()
            for neighbor in n.neighbors:
                if neighbor not in nodemap:
                    newneighbor = Node(neighbor.val)
                    nodemap[neighbor] = newneighbor
                    q.append(neighbor)
                nodemap[n].neighbors.append(nodemap[neighbor]) 
        
        return newnode

        