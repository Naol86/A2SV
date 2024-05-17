# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        for i in range(len(matrix) - 2, -1, -1):
            for j in range(len(matrix[0])):
                left = float('inf') if j == 0 else matrix[i+1][j-1]
                right = float('inf') if j == len(matrix[0]) - 1 else matrix[i+1][j+1]
                matrix[i][j] += min(matrix[i+1][j], left, right)
        # print(matrix)
        return min(matrix[0])