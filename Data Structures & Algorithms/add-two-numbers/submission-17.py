# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        
        cur1 = l1
        cur2 = l2
        dummy = ListNode()
        cur = dummy

        leftover = 0
        while cur1 or cur2 or leftover:
            a = cur1.val if cur1 else 0
            b = cur2.val if cur2 else 0

            value = a + b + leftover

            leftover = value //10
            cur.next= ListNode(value%10)

            if cur1:
                cur1 = cur1.next
          
            if cur2:
                cur2 = cur2.next
        
            cur = cur.next

        return dummy.next

            

            

            