# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def to_stack(self, head):
        stack = []
        while head:
            stack.append(head)
            head = head.next
        return stack

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = self.to_stack(head)
        leng = len(stack)
        current = head
        count = 0
        while count < leng//2:
            if head.val != stack.pop().val:
                return False
            head = head.next
            count += 1
        return True 