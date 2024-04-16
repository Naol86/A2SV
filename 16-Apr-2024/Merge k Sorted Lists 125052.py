# Problem: Merge k Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i in range(len(lists)):
            num = lists[i]
            if num:
                heapq.heappush(heap, (num.val, i))
        ans = ListNode(0)
        node = ans
        while heap:
            pop = heapq.heappop(heap)
            node.next = lists[pop[1]]
            if lists[pop[1]].next:
                heapq.heappush(heap, (lists[pop[1]].next.val, pop[1]))
                lists[pop[1]] = lists[pop[1]].next
            node = node.next

        # print(heap)
        return ans.next