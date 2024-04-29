# Problem: Similar String Groups - https://leetcode.com/problems/similar-string-groups/

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        rep = 0
        parent = [i for i in range(len(strs))]
        size = [1 for i in range(len(strs))]
        ans = [len(strs)]

        def find(x):
            if x == parent[x]:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            par_x = find(x)
            par_y = find(y)
            if par_y != par_x:
                ans[0] -= 1
                if size[par_x] > size[par_y]:
                    parent[par_y] = par_x
                    size[par_x] += size[par_y]
                else:
                    parent[par_x] = par_y
                    size[par_y] += size[par_x]
        
        for i in range(len(strs)):
            for j in range(i+1, len(strs)):
                count = 0
                for k in range(len(strs[0])):
                    if strs[i][k] != strs[j][k]:
                        count += 1
                    if count == 3:
                        break
                else:
                    union(i, j)
        return ans[0]