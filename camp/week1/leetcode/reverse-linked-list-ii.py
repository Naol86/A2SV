# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        self.last = None
        def helper(node, x):
            self.last = node.next
            if x < right:
                self.left.next = helper(node.next, x+1)
                self.left = self.left.next
                self.left.next = None

            return node

        dummy = ListNode('x',head)
        cur = dummy
        x = 1
        while cur:

            if x == left:
                self.left = cur
                self.left.next = helper(cur.next, x)
                self.left = self.left.next
                break
            else:
                cur = cur.next
                x += 1
        if left == 1:
            head = self.left
        self.left.next = self.last
        return dummy.next

