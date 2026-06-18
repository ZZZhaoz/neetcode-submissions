# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        pre = None
        while curr:
            if pre and pre.val > curr.val:
                return True
            pre = curr
            curr = curr.next
            
        return False
        