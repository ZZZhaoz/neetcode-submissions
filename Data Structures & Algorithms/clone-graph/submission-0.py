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
        
      
        q = collections.deque()
        oldToNew = {}
        oldToNew[node] = Node(node.val)
        q.append(node)
        
        while q:
            new_node = q.popleft()
            
            for neighbor in new_node.neighbors:
                
                if neighbor not in oldToNew:
                    q.append(neighbor)
                    oldToNew[neighbor] = Node(neighbor.val)
                    
                    

                oldToNew[new_node].neighbors.append(oldToNew[neighbor])
        return oldToNew[node]

        