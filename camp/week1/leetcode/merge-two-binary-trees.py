# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        node1 = root1
        node2 = root2
        if node1 == None and node2 != None:
            return node2
        if node1 != None and node2 == None:
            return node1
        if node1 == None or node2 == None:
            return None
        node1.val = node1.val + node2.val
        if node1.left == None:
            node1.left = node2.left
            node2.left = None
        if node1.right == None:
            node1.right = node2.right
            node2.right = None

        self.mergeTrees(node1.left, node2.left)
        self.mergeTrees(node1.right, node2.right)
        return node1
