# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self._dict = defaultdict(int)
        self.ans = []

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def help(node):
            if node == None:
                return
            self._dict[node.val] += 1
            if not self.ans:
                self.ans.append((node.val, self._dict[node.val]))
            else:
                if self.ans[-1][-1] == self._dict[node.val]:
                    self.ans.append((node.val, self._dict[node.val]))
                elif self.ans[-1][-1] < self._dict[node.val]:
                    self.ans = [(node.val, self._dict[node.val])]
            help(node.left)
            help(node.right)
        help(root)
        ans = [i for i, j in self.ans]
        return ans