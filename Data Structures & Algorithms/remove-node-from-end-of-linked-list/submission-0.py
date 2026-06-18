# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
            if head == []:
                return head
            else:
                curr = head
                previous = None
                while curr is not None:
                    temp = curr
                    curr = curr.next
                    temp.next = previous
                    previous = temp
                return previous
        head = reverseList(self, head)
        i = 1
        curr = head
        pre = None
        if n == 1:
            curr = curr.next
            return reverseList(self, curr)
        while curr:
            if i == n:
                
                temp = curr.next
                pre.next = temp
               
                

            pre = curr
            curr = curr.next
            i += 1
        return reverseList(self, head)
            