# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = defaultdict(list)

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def helper(node, level):
            if node is None:
                return level
            self.ans[level].append(node.val)
            left = helper(node.left, level + 1)
            right = helper(node.right, level + 1)
            return max(left, right)
        ans = [[0]] * helper(root, 0)
        for key, value in self.ans.items():
            if key % 2 != 0:
                ans[key] = value[::-1]
            else:
                ans[key] = value
        return ans