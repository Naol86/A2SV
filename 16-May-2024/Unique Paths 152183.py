# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[0] * (n + 1) for _ in range(m + 1)]
        matrix[1][1] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                matrix[i][j] += matrix[i-1][j] + matrix[i][j-1]
        # print(matrix)
        return matrix[-1][-1]
