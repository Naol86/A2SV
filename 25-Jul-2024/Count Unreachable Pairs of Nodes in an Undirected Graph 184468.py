# Problem: Count Unreachable Pairs of Nodes in an Undirected Graph - https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        elementes = [[i] for i in range(n)]
        size = [1 for _ in range(n)]
        def find(x):
            if x == parent[x]:
                return x
            x = find(parent[x])
            return parent[x]
        
        def union(x, y):
            if parent[x] != parent[y]:
                par_x = find(x)
                par_y = find(y)
                size_x = size[par_x]
                size_y = size[par_y]
                if size_x > size_y:
                    elementes[par_x].extend(elementes[par_y])
                    elementes[par_y] = []
                    parent[par_y] = par_x
                    size[par_x] += size[par_y]
                else:
                    elementes[par_y].extend(elementes[par_x])
                    parent[par_x] = par_y
                    elementes[par_x] = []
                    size[par_y] += size[par_x]
        
        for i, j in edges:
            union(i, j)
        # print(elementes)
        count = 0
        for lis in elementes:
            count += len(lis) * (n - len(lis))
        return count//2
        
        