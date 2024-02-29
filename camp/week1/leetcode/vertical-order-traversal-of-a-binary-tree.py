# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = defaultdict(list)
        self._min = 0
        self._max = 0

    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        def helper(node, x, y):
            if node is None:
                return None
            # if node.left is None and node.right is None:
            self._min = min(self._min, x)
            self._max = max(self._max, x)
            self.ans[x].append((y, node.val))
            if node.left is not None:
                helper(node.left, x - 1, y + 1)
            if node.right is not None:
                helper(node.right, x + 1, y + 1)
        helper(root, 0, 0)
        leng = self._max - self._min + 1
        ans = [0] * leng
        for key, value in self.ans.items():
            ans[-self._min + key] = sorted(value)
        final_ans = []
        for i in ans:
            temp = []
            for j in i:
                temp.append(j[1])
            final_ans.append(temp)
        return final_ans