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
                a = mergeTwoLists(self, lists[0], lists[1])
                lists.pop(0)
                lists.pop(0)
                lists.insert(0, a)
        return None

          