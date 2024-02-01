# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def creatPrev(node,prev):
            node.pre = prev
        head.pre = None
        temp = head

        while(temp.next):
            creatPrev(temp.next,temp)
            temp = temp.next
        left = head
        while(left.next):
            right = left.next
            while(right and right.pre):
                if right.val < right.pre.val:
                    right.val , right.pre.val = right.pre.val,right.val
                    right = right.pre
                else:
                    break
            left = left.next
        return head