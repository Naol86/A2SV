# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nums = []
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            nums.append(node.val)
            inorder(node.right)
        inorder(root)
        def balance(i, j):
            print(i, j)
            if i >= j:
                return None
            mid = (j + i) // 2
            node = TreeNode(nums[mid])
            node.left = balance(i, mid)
            node.right = balance(mid + 1, j)
            return node
        return balance(0, len(nums))