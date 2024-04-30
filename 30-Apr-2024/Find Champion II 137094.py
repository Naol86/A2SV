# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        in_degree = [0] * n
        for a, b in edges:
            in_degree[b] += 1
        ans = []
        for i in range(n):
            if in_degree[i] == 0:
                ans.append(i)
        if len(ans) != 1:
            return -1
        return ans[0]