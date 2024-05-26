# Problem: Construct String from Binary Tree - https://leetcode.com/problems/construct-string-from-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root == None:
            return ""
        if root.left == None and root.right == None:
            return str(root.val)
        if root.right == None:
            return f"{root.val}({self.tree2str(root.left)})"
        ans = f"{root.val}({self.tree2str(root.left)})({self.tree2str(root.right)})"
        return ans