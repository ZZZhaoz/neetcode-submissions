# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            dummy = new = ListNode()
            while list1 and list2:
                if list1.val < list2.val:
                    new.next = list1
                    list1 = list1.next
                else:
                    new.next = list2
                    list2 = list2.next
                new = new.next
            new.next = list1 or list2
            return dummy.next

          
 
        while lists:
            if len(lists) == 1:
                return lists[0]
            else:  
                merged = []
                for i in range(0 , len(lists), 2):
                    l1 = lists[i]
                    l2 = lists[i + 1] if (i + 1) < len(lists) else None

                    merged.append(mergeTwoLists(self, l1, l2))
                lists = merged
        return None

          