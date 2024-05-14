# Problem: Longest Common Subsequence - https://leetcode.com/problems/longest-common-subsequence/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        matrix = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        for i in range(len(text1)):
            for j in range(len(text2)):
                matrix[i+1][j+1] = max(matrix[i][j+1],matrix[i+1][j])
                if text1[i] == text2[j]:
                    matrix[i+1][j+1] = matrix[i][j] + 1
        return matrix[-1][-1]