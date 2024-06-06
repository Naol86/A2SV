# Problem: Maximum Depth of N-ary Tree - https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        self.ans = 0
        def dfs(node, depth):
            if not node:
                self.ans = max(self.ans, depth)
                return 

            if not node.children:
                self.ans = max(self.ans, depth + 1)
                return 
            for child in node.children:
                dfs(child, depth + 1)
        dfs(root , 0)
        return self.ans