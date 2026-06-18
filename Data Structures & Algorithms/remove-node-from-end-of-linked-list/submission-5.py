# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        rehead = self.reverseList(head)
        pre = None
        cur = rehead
        i = 1
        while cur and i != n:
            pre = cur
            cur = cur.next
            i += 1
        if pre:
            pre.next = cur.next
        else:
            rehead = rehead.next
        
        return self.reverseList(rehead)
 
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        while cur is not None:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        
        return pre

