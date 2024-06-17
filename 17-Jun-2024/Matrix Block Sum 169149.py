# Problem: Matrix Block Sum - https://leetcode.com/problems/matrix-block-sum/

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        prefix = [[0] * (len(mat[0]) + 1) for i in range(len(mat) + 1)]
        for i in range(1, len(prefix)):
            for j in range(1, len(prefix[0])):
                prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1] + mat[i-1][j-1]
        # for i in prefix:
        #     print(*i)
        ans = [[0] * len(mat[0]) for i in range(len(mat))]
        for i in range(1, len(mat) + 1):
            for j in range(1, len(mat[0]) + 1):
                left = j - k - 1 if j - k > 0 else 0
                right = j + k if j + k <= len(mat[0]) else len(mat[0])
                up = i - k - 1 if i - k > 0 else 0
                down = i + k if i + k <= len(mat) else len(mat)
                ans[i-1][j-1] = prefix[down][right] + prefix[up][left] - prefix[up][right] - prefix[down][left]
                
        

        return ans