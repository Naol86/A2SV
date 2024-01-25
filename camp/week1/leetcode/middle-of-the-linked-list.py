# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lis = []
        leng = 0
        while head:
            lis.append(head)
            head = head.next
            leng += 1
        return lis[leng//2]