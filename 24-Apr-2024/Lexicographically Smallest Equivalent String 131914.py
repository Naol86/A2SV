# Problem: Lexicographically Smallest Equivalent String - https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = defaultdict()
        for s in s1:
            parent[s] = s
        for s in s2:
            parent[s] = s
        # print(parent)

        def find(x):
            if x not in parent:
                return x
            if x == parent[x]:
                return x
            x = find(parent[x])
            return x
        
        def union(x, y):
            parentX = find(x)
            parentY = find(y)

            if parentX == parentY:
                return True
            elif parentX < parentY:
                parent[parentY] = parentX
            else:
                parent[parentX] = parentY
        
        for i in range(len(s1)):
            union(s1[i], s2[i])
        
        ans = []
        for s in baseStr:
            ans.append(find(s))


        return ''.join(ans)