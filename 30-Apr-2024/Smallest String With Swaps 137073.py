# Problem: Smallest String With Swaps - https://leetcode.com/problems/smallest-string-with-swaps/

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        x = len(s)
        ans = [[s[i]] for i in range(x)]
        parent = [i for i in range(x)]
        size = [1 for i in range(x)]
        pos = [0 for i in range(x)]
        def find(x):
            if x == parent[x]:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            par_x = find(x)
            par_y = find(y)
            if par_x != par_y:
                if size[par_x] > size[par_y]:
                    parent[par_y] = par_x
                    size[par_x] += size[par_y]
                    ans[par_x].extend(ans[par_y])
                    ans[par_y] = []
                else:
                    parent[par_x] = par_y
                    size[par_y] += size[par_x]
                    ans[par_y].extend(ans[par_x])
                    ans[par_x] = []
        for a, b in pairs:
            union(a, b)
        st = []
        for i in range(x):
            ans[i].sort()
        for i in range(x):
            temp = find(i)
            st.append(ans[temp][pos[temp]])
            pos[temp] += 1
        # print(ans)
        return ''.join(st)