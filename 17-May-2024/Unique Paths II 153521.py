# Problem: Unique Paths II - https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1] or obstacleGrid[0][0]:
            return 0
        dp = [[0] * (len(obstacleGrid[0]) + 1) for _ in range(len(obstacleGrid) + 1)]
        dp[1][1] = 1
        # print(dp)
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if obstacleGrid[i-1][j-1]:
                    continue
                dp[i][j] += dp[i-1][j] + dp[i][j-1]
        # print(dp)
        
        return dp[-1][-1]