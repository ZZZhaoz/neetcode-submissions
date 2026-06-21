# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        head2 = self.reverseList(slow.next)
        slow.next = None

        list1 = head
        list2 = head2
        while list1 and list2:
            temp1 = list1.next
            temp2 = list2.next
            list1.next = list2
            list2.next = temp1
            list1 = temp1
            list2 = temp2

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        while cur is not None:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        
        return pre