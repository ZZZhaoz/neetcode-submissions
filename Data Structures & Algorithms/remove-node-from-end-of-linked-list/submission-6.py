# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        rehead = self.reverseList(head)
        prev = None
        cur = rehead
        i = 1
        while cur:
            if prev and i == n:
                prev.next = cur.next
            elif not prev and i == n:
                rehead = cur.next
            else:
                prev = cur
                cur = cur.next
            i += 1
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

