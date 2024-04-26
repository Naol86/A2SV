# Problem: Parallel Courses III - https://leetcode.com/problems/parallel-courses-iii/

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = [[] for _ in range(n+1)]
        in_degree = [0] * (n+1)
        ans = [0] * (n+1)
        for x, y in relations:
            graph[x].append(y)
            in_degree[y] += 1
        
        queue = deque()
        _max = 0
        for i in range(1, n+1):
            if in_degree[i] == 0:
                queue.append(i)
                _max = max(time[i-1], _max)
                ans[i] = time[i-1]

        while queue:
            x = queue.popleft()
            # _max = max(time[x], _max)
            for node in graph[x]:
                ans[node] = max(ans[node], ans[x])
                in_degree[node] -= 1
                if in_degree[node] == 0:
                    queue.append(node)
                    ans[node] += time[node-1]
        return max(ans)

