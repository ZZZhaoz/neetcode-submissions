# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        dummy = ListNode()
        cur = dummy
        temp = 0
        while curr1 and curr2:
            
            if curr1.val + curr2.val <= 9:
                cur.next = ListNode(curr1.val + curr2.val + temp)
                temp = 0
            else:
                cur.next= ListNode(curr1.val + curr2.val + temp - 10)
                temp = 1
            cur = cur.next
            curr1 = curr1.next
            curr2 = curr2.next
        while curr1 or curr2:
            if curr1:
                if temp + curr1.val >= 10:
                    cur.next = ListNode(0)
                    temp = 1
                else:
                    cur.next = ListNode(temp + curr1.val)
                    temp = 0
                curr1 = curr1.next
            
            else:
                if temp + curr2.val >= 10:
                    cur.next = ListNode(0)
                    temp = 1
                else:
                    cur.next = ListNode(temp + curr2.val)
                    temp = 0
                curr2 = curr2.next
            cur = cur.next

        
        if temp == 1:
            cur.next = ListNode(1)
        
        return dummy.next

            

            

        