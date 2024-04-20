# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        leng = len(graph)
        outDegree = [0] * leng
        nodes = [[] for i in range(leng)]
        queue = deque()
        ans = []
        for i in range(leng):
            for node in graph[i]:
                nodes[node].append(i)
            outDegree[i] += len(graph[i])
            if outDegree[i] == 0:
                ans.append(i)
                queue.append(i)
        while queue:
            x = queue.popleft()
            for node in nodes[x]:
                outDegree[node] -= 1
                if outDegree[node] == 0:
                    ans.append(node)
                    queue.append(node)
        ans.sort()
        return ans