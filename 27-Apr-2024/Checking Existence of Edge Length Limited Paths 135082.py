# Problem: Checking Existence of Edge Length Limited Paths - https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        ans = [False] * len(queries)
        edgeList.sort(key=lambda x: x[-1])
        for i in range(len(queries)):
            queries[i].append(i)
        queries.sort(key=lambda x: x[2])
        print(queries)
        print(edgeList)
        parent = [i for i in range(n)]
        size = [1 for i in range(n)]
        def find(x):
            if x == parent[x]:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            parent_x = find(x)
            parent_y = find(y)
            if parent_x != parent_y:
                if size[parent_x] > size[parent_y]:
                    parent[parent_y] = parent_x
                    size[parent_x] += size[parent_y]
                else:
                    parent[parent_x] = parent_y
                    size[parent_y] += size[parent_x]
        
        i = 0
        j = 0
        while i < len(queries):
            x, y, dis, indx = queries[i]
            while j < len(edgeList) and edgeList[j][-1] < dis:
                union(edgeList[j][0], edgeList[j][1])
                j += 1
                
            i += 1
            parent_x = find(x)
            parent_y = find(y)
            # print(parent)
            if parent_x == parent_y:
                ans[indx] = True
        return ans
