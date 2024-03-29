# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def help(left, right):
            if left == None and right == None:
                return True
            if left == None and right != None:
                return False
            if left != None and right == None:
                return False
            if left.val != right.val:
                return False
            l = help(left.left, right.right)
            r = help(left.right, right.left)
            return l and r
        return help(root.left, root.right)
