class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = row
        max_row = [0] * row
        max_col = [0] * col
        for i in range(row):
            for j in range(col):
                max_row[i] = max(max_row[i], grid[i][j])
                max_col[j] = max(max_col[j], grid[i][j])
        count = 0
        for i in range(row):
            for j in range(col):
                count += min(max_row[i], max_col[j]) - grid[i][j]
        return count