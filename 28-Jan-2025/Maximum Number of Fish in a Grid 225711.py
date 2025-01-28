# Problem: Maximum Number of Fish in a Grid - https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        _max = 0

        visited = set()
        def check(i, j):
            if (i, j) in visited:
                return 0
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return 0
            if grid[i][j] == 0:
                return 0
            visited.add((i, j))
            return grid[i][j] + check(i - 1, j) + check(i + 1, j) + check(i, j + 1) + check(i, j - 1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) in visited or grid[i][j] == 0:
                    continue
                # print(i, j)
                _max = max(_max, check(i, j))
        
        return _max