# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def find(node):
            if node is None:
                return None
            if node.val == key:
                return node
            if node.val > key:
                return find(node.left)
            return find(node.right)
        node = find(root)
        if node is None:
            return root
        # print(node.val)

        def delete(node, cur, replace):
            if node is None:
                return False
            if node.val == cur.val:
                node = replace
                return node
            if node.left and node.left.val == cur.val:
                node.left = replace
                return False
            if node.right and node.right.val == cur.val:
                node.right = replace
                return False
            if node.val > cur.val:
                return delete(node.left, cur, replace)
            return delete(node.right, cur, replace)
        def find_max(node):
            if node.right is None:
                return node
            return find_max(node.right)

        if node.left is None and node.right is None:
            x = delete(root, node, None)
            if x != False:
                return x
            return root
        if node.left is None and node.right is not None:
            # delete(root, node, node.right)
            # return root
            x = delete(root, node, node.right)
            if x != False:
                return x
            return root
        if node.right is None and node.left is not None:
            # delete(root, node, node.left)
            # return root
            x = delete(root, node, node.left)
            if x != False:
                return x
            return root
        if node.right is not None and node.left is not None:
            _max = find_max(node.left)
            # print(_max)
            self.deleteNode(root, _max.val)
            node.val = _max.val
        return root