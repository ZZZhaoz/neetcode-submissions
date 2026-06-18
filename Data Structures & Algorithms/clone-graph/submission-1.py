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

        oldToNew = {}
        oldToNew[node] = Node(node.val)
        q = deque([node])

        while q:
            n = q.popleft()
            for neighbor in n.neighbors:
                if neighbor not in oldToNew:
                    oldToNew[neighbor] = Node(neighbor.val) 
                    q.append(neighbor)   
                oldToNew[n].neighbors.append(oldToNew[neighbor])    
                  

        return oldToNew[node]   

        