# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        cur1 = list1
        cur2 = list2
        currnew = new = ListNode()

        while cur1 and cur2:
            if cur1.val < cur2.val:
                currnew.next = cur1
                cur1 = cur1.next

            else:
                currnew.next = cur2
                cur2 = cur2.next

            currnew = currnew.next

        if cur1 is None:
            currnew.next = cur2
        
        if cur2 is None:
            currnew.next = cur1

        return new.next

        