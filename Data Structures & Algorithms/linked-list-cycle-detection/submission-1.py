# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = []
        cur = head
        visited.append(cur)
        while cur is not None:
            if cur.next in visited:
                return True
            else:
                cur = cur.next
                visited.append(cur)
           
        return False

        