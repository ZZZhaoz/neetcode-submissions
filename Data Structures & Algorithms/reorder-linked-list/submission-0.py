# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
            if not head:  # Correct empty list check
                return head
            previous = None
            curr = head
            while curr:
                temp = curr.next
                curr.next = previous
                previous = curr
                curr = temp
            return previous

        if not head or not head.next:  # If the list is empty or has only one node
            return

        # Step 1: Find the midpoint using the slow and fast pointer approach
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half of the list
        second = slow.next
        slow.next = None  # Split the list into two halves
        second = reverseList(second)

        # Step 3: Merge the two halves
        current = head
        current2 = second
        while current2:
            temp = current.next
            temp2 = current2.next

            current.next = current2
            current2.next = temp

            current = temp
            current2 = temp2


            

        
