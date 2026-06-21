# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        cur1 = list1
        cur2 = list2
        dummy = ListNode()
        new = dummy

        while cur1 and cur2:
            if cur1.val < cur2.val:
                new.next = cur1
                cur1 = cur1.next
            else:
                new.next = cur2
                cur2 = cur2.next
            new = new.next
        
        if cur1:
            new.next = cur1
        else:
            new.next = cur2
        return dummy.next
        