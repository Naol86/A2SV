class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        if row == 3 and col == 3:
            _sum = sum(grid[0]) + sum(grid[-1]) + grid[1][1]
            return _sum
        lis = [[0] * (len(grid[0])+1) for i in range(len(grid)+1)]
        for i in range(1,row+1):
            for j in range(1,col+1):
                lis[i][j] = lis[i][j-1] + grid[i-1][j-1]
        _max = 0
        for i in range(1,row-1):
            for j in range(3,col+1):
                temp = lis[i][j] + lis[i+2][j] + lis[i+1][j-1] - lis[i][j-3] - lis[i+2][j-3] - lis[i+1][j-2]
                _max = max(_max, temp)
        return _max
