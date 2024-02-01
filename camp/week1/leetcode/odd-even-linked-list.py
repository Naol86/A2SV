# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        odd_head = ListNode('a') 
        even_head = ListNode('a')
        odd = odd_head
        even = even_head
        current = head
        i = 0
        while current:
            if i % 2 != 0:
                odd.next = current
                odd = odd.next
            else:
                even.next = current
                even = even.next
            current = current.next
            i += 1
        odd.next = None
        even.next = None
        even.next = odd_head.next
        return even_head.next
                