# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        current = root
        if current.val == p.val or current.val == q.val:
            return current
        if current.val > p.val and current.val < q.val:
            return current
        if current.val < p.val and current.val > q.val:
            return current
        if current.val > p.val:
            return self.lowestCommonAncestor(current.left, p, q)
        return self.lowestCommonAncestor(current.right, p, q)