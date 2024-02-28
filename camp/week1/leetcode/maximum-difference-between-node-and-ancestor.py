# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        _max = root.val
        _min = root.val
        diff = _max - _min
        def find(node, _max, _min, diff):
            if node is None:
                return diff
            if node.val > _max:
                _max = node.val
                diff = _max - _min
            elif node.val < _min:
                _min = node.val
                diff = _max - _min
            left = find(node.left, _max, _min, diff)
            right = find(node.right, _max, _min, diff)
            return max(left, right)
        
        left = find(root.left, _max, _min, 0)
        right = find(root.right, _max, _min, 0)
        return max(left, right)
