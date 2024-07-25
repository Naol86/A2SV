# Problem: Merge Nodes in Between Zeros - https://leetcode.com/problems/merge-nodes-in-between-zeros

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode(0)
        ans = root
        cur = head.next
        while cur:
            if cur.val:
                root.val += cur.val
            else:
                if cur.next:
                    root.next = ListNode()  
                    root = root.next
                # cur = cur.next
            cur = cur.next
        return ans