# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        # we need max value from left side
        # we need min value from right side
        def helper(node, left):
            if node is None:
                return (0, 0, float('inf'))
            if node.left is None and node.right is None:
                self.ans = max(self.ans, node.val)
                return (node.val, node.val, node.val)
            l = helper(node.left, True) if node.left is not None else (0,node.val - 1,node.val)
            r = helper(node.right, False) if node.right is not None else (0,node.val,node.val + 1)
            # print(l,r, node.val)
            if l and r and l[1] < node.val < r[2]:
                _sum = node.val + l[0] + r[0]
                self.ans = max(self.ans, _sum)
                # print(self.ans, node.val)
                return (_sum, max(l[1], r[1]), min(l[2], r[2]))
            else:
                return False
        left = helper(root, True)
        # print(self.ans)
        if self.ans < 0:
            return 0
        return self.ans