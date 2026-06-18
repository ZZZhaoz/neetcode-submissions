# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
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
         # Calculate the length of the list
        length = 0
        current = head
        while current:
            current = current.next
            length += 1

        dummy = ListNode(0)
        dummy.next = head
        prev_tail = dummy
        current = head

        while length >= k:
            group_head = current
            # Move the pointer to the end of the group
            for _ in range(k - 1):
                current = current.next
            
            next_group = current.next
            current.next = None  # Disconnect the group
            # Reverse the group
            reversed_group = reverseList(self, group_head)
            # Connect the previous part with the reversed group
            prev_tail.next = reversed_group
            # Connect the end of the reversed group to the next group
            group_head.next = next_group
            # Update pointers for the next iteration
            prev_tail = group_head
            current = next_group
            length -= k
        
        return dummy.next