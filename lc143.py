# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head.next:
            return head
        if not head.next.next:
            return head
        first, second = head, head.next
        while second and second.next:
            first = first.next
            second=second.next.next
        
        half_2 = first.next
        half_1 = head.next
        first.next=None
        prev = None
        
        while half_2:
            temp = half_2.next
            half_2.next = prev
            prev = half_2
            if not temp:
                break
            half_2 = temp
    
        head.next = None

        cur = head
        
        i = 0
        while half_2:
            a = half_2.next
            b = half_1.next if half_1 else None
            cur.next = half_2
            half_2.next = half_1
            half_2 = a
            cur = half_1
            half_1 = b
            
            