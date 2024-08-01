# Problem: Binary Tree Right Side View - https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.dic = {}
        
        def traver(depth, node):
            if node is None:
                return
  
            self.dic[depth] = node.val
            traver(depth + 1, node.left)
            traver(depth + 1, node.right)
        
        traver(0, root)
        
        ans = [0] * len(self.dic)
        for depth, val in self.dic.items():
            ans[depth] = val
        
        return ans