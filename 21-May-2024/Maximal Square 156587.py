# Problem: Maximal Square - https://leetcode.com/problems/maximal-square/

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        grid = [[[0,0] for _ in range(len(matrix[0]) + 1)] for __ in range(len(matrix) + 1)]
        ans = 0
        for i in range(1, len(matrix) + 1):
            for j in range(1, len(matrix[0]) + 1):
                if matrix[i-1][j-1] == '0':
                    continue
                grid[i][j][0] = min(grid[i][j-1][0], grid[i-1][j][0], grid[i-1][j-1][0]) + 1
                grid[i][j][1] = min(grid[i][j-1][1], grid[i-1][j][1], grid[i-1][j-1][1]) + 1
                ans = max(ans, min(grid[i][j]) ** 2)
        # for g in grid:
        #     print(*g)
        return ans