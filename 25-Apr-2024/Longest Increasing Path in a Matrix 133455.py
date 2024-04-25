# Problem: Longest Increasing Path in a Matrix - https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        cache = defaultdict(list)
        pos = [(0,1), (0,-1), (1,0),(-1,0)]
        def indx(nums):
            return nums.index(max(nums))

        def dfs(x, y):
            # up down left right
            if (x, y) in cache:
                return cache[(x, y)]
            up = []
            if x > 0 and matrix[x][y] < matrix[x-1][y]:
                up.extend(dfs(x - 1, y))
            down = []
            if x < len(matrix) - 1 and matrix[x][y] < matrix[x + 1][y]:
                down.extend(dfs(x + 1, y))
            left = []
            if y > 0 and matrix[x][y] < matrix[x][y-1]:
                left.extend(dfs(x, y - 1))
            right = []
            if y < len(matrix[0]) - 1 and matrix[x][y] <matrix[x][y + 1]:
                right.extend(dfs(x, y + 1))
            
            ans = indx([len(up), len(down), len(left), len(right)])
            final_ans = [matrix[x][y]]
            if ans == 0:
                final_ans.extend(up)
            if ans == 1:
                final_ans.extend(down)
            if ans == 2:
                final_ans.extend(left)
            if ans == 3:
                final_ans.extend(right)
            cache[(x, y)] = final_ans
            # print(final_ans)
            return final_ans

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dfs(i, j)
            # print(cache)
        _max = 0
        for key, value in cache.items():
            if _max < len(value):
                _max = len(value)
        # print(ans)
        return _max