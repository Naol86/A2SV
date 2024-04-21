# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        leng = len(quiet)
        # ans = [0] * leng
        inDegree = [0] * leng
        graph = [[] for _ in range(leng)]
        ans = [i for i in range(leng)]
        for a, b in richer:
            inDegree[b] += 1
            graph[a].append(b)
        queue = deque()
        for i in range(leng):
            if inDegree[i] == 0:
                queue.append(i)
        # print(graph)
        # print(inDegree)
        # print(queue)
        while queue:
            x = queue.popleft()
            for node in graph[x]:
                if quiet[ans[node]] > quiet[ans[x]]:
                    ans[node] = ans[x]
                # print(f"parent {x} --> {node} --- ", ans[x], ans[node],)
                inDegree[node] -= 1
                if inDegree[node] == 0:
                    queue.append(node)
        return ans