# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        def build(lis):
            if lis == []:
                return None
            node = ListNode(lis[0])
            for i in lis[1:]:
                node = ListNode(i, node)
            return node
        def to_array(node):
            lis = []
            while node:
                lis.append(node.val)
                node = node.next
            return lis
        lis = to_array(head)
        leng = len(lis)
        val = leng // k
        ans = []
        index = 0
        for i in range(leng % k):
            ans.append(lis[index: index + val + 1])
            index += val + 1
        val = val if val > 0 else 1
        for i in range(k - (leng % k)):
            ans.append(lis[index: index + val])
            index += val
        nodes = []
        for i in ans:
            a = build(i[::-1])
            nodes.append(a)
        return nodes