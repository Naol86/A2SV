# Problem: Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def distance(x, y):
            return abs(x[0] - y[0]) + abs(x[1] - y[1])
        edges = []
        leng = len(points)
        visited = [leng]
        for i in range(leng):
            for j in range(i + 1, leng):
                dis = distance(points[i], points[j])
                edges.append((dis, i, j))
        edges.sort()

        parent = [i for i in range(leng)]
        size = [1 for _ in range(leng)]
        def find(x):
            if x == parent[x]:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            par_x = find(x)
            par_y = find(y)
            if par_x != par_y:
                visited[0] -= 1
                if size[par_x] > size[par_y]:
                    parent[par_y] = par_x
                    size[par_x] += size[par_y]
                else:
                    parent[par_x] = par_y
                    size[par_y] += size[par_x]
                return True
            return False
        # visited = set()
        i = 0
        ans = 0
        # print(edges)
        while visited[0] > 1:
            dis, x, y = edges[i]
            temp = union(x, y)
            i += 1
            if not temp:
                continue
            ans += dis
        return ans