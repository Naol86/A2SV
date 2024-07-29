# Problem: Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/

from copy import deepcopy
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        mat = deepcopy(matrix)
        row = len(matrix)
        col = len(matrix[0])
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    # print(i,j)
                    for _ in range(row):
                        matrix[_][j] = 0
                    for _ in range(col):
                        matrix[i][_] = 0
                    # print(matrix)
        return matrix
        