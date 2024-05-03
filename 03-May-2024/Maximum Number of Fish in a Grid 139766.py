# Problem: Maximum Number of Fish in a Grid - https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        visited = set()
        _max = [0]
        pos = [(1,0), (-1,0),(0,1),(0,-1)]
        def check(i, j):
            if (i, j) in visited:
                return False
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return False
            if grid[i][j] == 0:
                return False
            return True

        def dfs(i, j):
            _sum = grid[i][j]
            queue = [(i, j)]
            while queue:
                x, y = queue.pop()
                for i, j in pos:
                    new_row = x + i
                    new_col = y + j
                    if check(new_row, new_col):
                        _sum += grid[new_row][new_col]
                        queue.append((new_row, new_col))
                        visited.add((new_row, new_col))
            _max[0] = max(_max[0], _sum)            

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0 and (i, j) not in visited:
                    visited.add((i, j))
                    dfs(i, j)
        
        return _max[0]