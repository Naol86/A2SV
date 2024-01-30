class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        col = len(matrix[0]) + 1
        row = len(matrix) + 1
        preFix = [[0] * col for _ in range(row)]

        for i in range(1, row):
            for j in range(1, col):
                preFix[i][j] = (matrix[i-1][j-1] -
                                preFix[i - 1][j - 1] +
                                preFix[i][j-1] + preFix[i-1][j])
        for i in preFix:
            print(*i)

        ans = 0
        for r in range(1, row):
            for c in range(1, col):
                for i in range(r - 1, -1, -1):
                    for j in range(c - 1, -1, -1):
                        # if preFix[r][c] == target:
                        #     ans += 1
                        #     continue
                        # if i == r and j == c:
                        #     continue
                        # print(preFix[r][c], preFix[i][j])
                        temp = (preFix[r][c] - preFix[r][j] -
                                preFix[i][c] + preFix[i][j])
                        if temp == target:
                            ans += 1
        return ans
