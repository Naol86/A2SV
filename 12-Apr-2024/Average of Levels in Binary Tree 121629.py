# Problem: Average of Levels in Binary Tree - https://leetcode.com/problems/average-of-levels-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque([root])
        ans = [root.val]
        while queue:
            x = len(queue)
            _sum = 0
            leng = 0
            while x > 0:
                temp = queue.popleft()
                x -= 1
                if temp.left:
                    queue.append(temp.left)
                    _sum += temp.left.val
                    leng += 1
                if temp.right:
                    queue.append(temp.right)
                    _sum += temp.right.val
                    leng += 1
            if leng:
                ans.append(_sum/leng)
        return ans

