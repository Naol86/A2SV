# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        pos = defaultdict(lambda: float('inf'))
        self.ans = 0
        def helper(node, level, left):
            if node is None:
                return
            pos[level] = min(pos[level], left)
            self.ans = max(left - pos[level] + 1, self.ans)
            helper(node.left, level + 1, left * 2)
            helper(node.right, level + 1, left * 2 + 1)
        
        helper(root, 0, 0)
        # print(self.ans)
        return self.ans