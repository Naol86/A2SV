# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    def __init__(self):
        self.visited = {}

    def uniquePaths(self, m: int, n: int) -> int:
        def helper(row, col):
            if (row, col) in self.visited:
                return self.visited[(row, col)]
            elif row == m - 1 and col == n - 1:
                return 1
            down = 0 if row >= m - 1 else helper(row + 1, col)
            upper = 0 if col >= n - 1 else helper(row, col + 1)
            res = down + upper
            self.visited[(row, col)] = res
            return res
        return helper(0, 0)