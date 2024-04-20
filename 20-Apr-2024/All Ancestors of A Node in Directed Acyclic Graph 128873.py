# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # graph = [[] for i in range(n)]
        nodes = [[] for i in range(n)]
        ans = [set() for i in range(n)]
        inDegree = [0 for i in range(n)]
        for parent, child in edges:
            nodes[parent].append(child)
            inDegree[child] += 1

        queue = deque()
        for i in range(n):
            if inDegree[i] == 0:
                queue.append(i)
        
        # print(nodes)
        # print(inDegree)
        # print(queue)
        while queue:
            x = queue.popleft()
            for node in nodes[x]:
                inDegree[node] -= 1
                if inDegree[node] == 0:
                    queue.append(node)
                ans[node].add(x)
                ans[node] = ans[node].union(ans[x])
        for i in range(n):
            ans[i] = list(ans[i])
            ans[i].sort()

        return ans