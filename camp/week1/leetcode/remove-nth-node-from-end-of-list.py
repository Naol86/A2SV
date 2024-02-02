# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode('x', head)
        cur = dummy
        count = 0
        while cur.next:
            count += 1
            cur = cur.next
        i = 0
        cur = dummy
        while cur.next and i < count - n:
            i += 1
            cur = cur.next
        cur.next = cur.next.next
        # print(cur.val) 
        return dummy.next