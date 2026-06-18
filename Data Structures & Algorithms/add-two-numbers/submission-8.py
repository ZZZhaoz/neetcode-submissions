# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0
        dummy = ListNode()
        curr = dummy
        while l1 or l2:
            if l1:
                v1 = l1.val
                l1 = l1.next
            else:
                v1 = 0
            if l2:
                v2 = l2.val
                l2 = l2.next
            else:
                v2 = 0
            total = v2 + v1 + carry
            carry = total // 10
            val = total % 10
            
            curr.next = ListNode(val, None)
            curr = curr.next

        if carry:
            curr.next = ListNode(1, None)
        return dummy.next

            

        