# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        currnew = new = ListNode()
        while curr1 and curr2:
            if curr1.val < curr2.val:
                currnew.next = curr1
                curr1 = curr1.next
                
            else:
                currnew.next = curr2
                curr2 = curr2.next
            currnew = currnew.next
        currnew.next = curr1 or curr2
        return new.next
          