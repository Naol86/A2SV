# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = {i:i for i in range(1, n + 1)}
        size = {i:1 for i in range(1, n + 1)}

        def find(x):
            if x == parent[x]:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        ans = []
        def union(x, y):
            parentX = find(x)
            parentY = find(y)
            sizeX = size[parentX]
            sizeY = size[parentY]

            if parentX == parentY:
                ans.append(x)
                ans.append(y)
                return True
            if sizeX > sizeY:
                parent[parentY] = parentX
                size[parentX] += size[parentY]
            else:
                parent[parentX] = parentY
                size[parentY] += size[parentX]
            return False
        for x, y in edges:
            temp = union(x, y)
            if temp:
                return ans
        return ans