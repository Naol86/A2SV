# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.lis = []
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder(node):
            if node is None:
                return 
            if node.left is None and node.right is None:
                self.lis.append(node.val)
                return
            if node.left is not None:
                inorder(node.left)
            self.lis.append(node.val)
            inorder(node.right)
            # inorder.append()
        inorder(root)
        for i in range(len(self.lis) - 1):
            if self.lis[i] >= self.lis[i + 1]:
                return False
        return True
            
