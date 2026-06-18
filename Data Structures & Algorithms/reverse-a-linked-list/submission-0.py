# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
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


        