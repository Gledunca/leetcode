# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        a, b = head, head
        for _ in range(n):
            b = b.next
        if not b:
            return a.next
        while b.next:
            a = a.next
            b = b.next
        a.next = a.next.next
        return head