# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(lis):
            if lis == []:
                return None
            _max = 0
            index = 0
            for i in range(len(lis)):
                if lis[i] > _max:
                    _max = lis[i]
                    index = i
            node = TreeNode(_max)
            node.left = helper(lis[:index])
            node.right = helper(lis[index + 1:])
            return node
        return helper(nums)