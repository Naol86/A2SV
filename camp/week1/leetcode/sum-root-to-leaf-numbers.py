# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        lis = []
        def helper(node, cur):
            if node is None:
                return
            if node.left is None and node.right is None:
                cur.append(str(node.val))
                lis.append(''.join(cur))
                return 
            else:
                cur.append(str(node.val))
                temp = deepcopy(cur)
                temp2 = deepcopy(cur)
                helper(node.left, temp)
                helper(node.right, temp2)
                return 
        helper(root, [])
        # print(lis)
        ans = 0
        for num in lis:
            ans += int(num)
        return ans