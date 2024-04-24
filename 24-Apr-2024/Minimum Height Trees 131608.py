# Problem: Minimum Height Trees - https://leetcode.com/problems/minimum-height-trees/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n < 3:
            return [i for i in range(n)]
        ans = set([i for i in range(n)])
        graph = [[] for _ in range(n)]
        inDegree = [0] * n
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            inDegree[a] += 1
            inDegree[b] += 1
        
        queue = deque()
        for i in range(n):
            if inDegree[i] == 1:
                queue.append(i)
                ans.remove(i)
        # print(queue)
        # print(inDegree)
        while len(ans) > 2:
            leng = len(queue)
            for _ in range(leng):
                x = queue.popleft()
                for node in graph[x]:
                    
                    if inDegree[node] <= 0:
                        continue
                    inDegree[node] -= 1
                    if inDegree[node] == 1:
                        queue.append(node)
                        ans.remove(node)
            # print(queue, ans)

        return list(ans)

        

        