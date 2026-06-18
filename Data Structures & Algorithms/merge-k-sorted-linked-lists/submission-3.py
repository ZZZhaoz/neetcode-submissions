# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        merged = lists[0]
        i = 0
        for lst in lists:
            i += 1
            if i == 1:
                continue
            merged = self.mergeTwoLists(merged, lst)
            
        return merged 

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
