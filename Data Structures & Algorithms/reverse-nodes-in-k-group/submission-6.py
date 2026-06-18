# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def getK(node):
            count = 0
            while node and count < k:
                node = node.next
                count += 1
            return count == k
            
        def reverseK(head, k):
                prev = None
                curr = head
                while k:
                    nxt = curr.next
                    curr.next = prev
                    prev = curr
                    curr = nxt
                    k -= 1
                return prev  #

        dummy = ListNode(0)
        dummy.next = head
        pre_group = dummy
        
        while getK(pre_group.next):
            tail = pre_group.next
            nxt_group_head = tail
            for _ in range(k):
                nxt_group_head = nxt_group_head.next
            new_head = reverseK(tail, k)
            pre_group.next = new_head
            tail.next = nxt_group_head
            pre_group = tail

        return dummy.next

   

        