# Problem: Minimum Score of a Path Between Two Cities - https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        minimum = [float('inf')] * n
        size = [1] * n
        parent = [i for i in range(n)]
        def find(x):
            if x == parent[x]:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y, c):
            par_x = find(x)
            par_y = find(y)
            if par_x != par_y:
                if size[par_x] > size[par_y]:
                    parent[par_y] = par_x
                    size[par_x] += size[par_y]
                    minimum[par_x] = min(minimum[par_x], minimum[par_y], c)
                else:
                    parent[par_x] = par_y
                    size[par_y] += size[par_x]
                    minimum[par_y] = min(minimum[par_x], minimum[par_y], c)
        
        for a, b, c in roads:
            pa, pb = find(a-1), find(b-1)
            minimum[pa] = min(minimum[pa], c)
            minimum[pb] = min(minimum[pb], c)
            union(a-1, b-1, c)
        return minimum[find(0)]