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
        mp = {}
        curr = head
        mp2 = {}
        if head:
            headval = head.val
        else:
            return head
        i = 0
        while curr:
            val = curr.val
          
            curr = curr.next
          
            mp[(val, i)] = Node(val, None, None)
            if val not in mp2:
                mp2[val] = i
            i += 1
        i = 0
            
        curr = head
        while curr:
           
            newcurr = mp[(curr.val, i)]
            if curr.next is None:
                newcurr.next = None
            else:
                newcurr.next = mp[(curr.next.val, i + 1)]
            if curr.random is None:
                newcurr.random = None
            else:
                newcurr.random = mp[(curr.random.val, mp2[curr.random.val])]
            curr = curr.next
            i += 1
        return mp[(head.val, 0)]