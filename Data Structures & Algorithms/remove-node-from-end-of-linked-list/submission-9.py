# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = slow

        if not fast.next:
            return

        for i in range(n):
            fast = fast.next

        if not fast:
            return head.next

        while fast:
            if not fast.next:
                slow.next = slow.next.next
                return head

            fast = fast.next
            slow = slow.next
    
        return head