# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur_1 = list1
        cur_2 = list2
        ans = None
        res = ans
        while cur_1 and cur_2:
            temp = None
            if cur_1.val < cur_2.val:
                temp = cur_1
                cur_1 = cur_1.next
            else:
                temp = cur_2
                cur_2 = cur_2.next
            if ans is None:
                ans = temp
                res = ans
            else:
                ans.next = temp
                ans = temp
        if ans is None:
            ans = cur_1 if cur_1 is not None else cur_2
            return ans
        if cur_1 is not None and ans:
            ans.next = cur_1
        if cur_2 is not None and ans:
            ans.next = cur_2
        return res
