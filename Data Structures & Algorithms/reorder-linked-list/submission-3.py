# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        head2= slow.next
        slow.next = None
           
        head2_r = self.reverseList(head2)  

        cur = head
        cur2 = head2_r

        while cur and cur2:
            temp = cur.next
            temp2 = cur2.next
            cur.next = cur2
            cur2.next = temp
            cur = temp
            cur2 = temp2

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        while cur is not None:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        
        return pre