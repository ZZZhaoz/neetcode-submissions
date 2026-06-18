"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mp = {None: None}
        
        curr = head
        while curr:
            val = curr.val
            mp[curr] = Node(val, None, None)
            curr = curr.next
          
        curr = head
        while curr:
            copy = mp[curr]
            copy.next = mp[curr.next]
            copy.random = mp[curr.random]        
          
            curr = curr.next
            
        return mp[head]