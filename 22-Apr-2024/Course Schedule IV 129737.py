# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        inDegree = [0] * numCourses
        graph = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            inDegree[b] += 1
            graph[a].append(b)
        ans = [set([i]) for i in range(numCourses)]
        queue = deque()
        for i in range(numCourses):
            if inDegree[i] == 0:
                queue.append(i)

        while queue:
            x = queue.popleft()
            for node in graph[x]:
                inDegree[node] -= 1
                ans[node] = ans[node].union(ans[x])
                if inDegree[node] == 0:
                    queue.append(node)
        final = []
        for u, v in queries:
            if u in ans[v]:
                final.append(True)
            else:
                final.append(False)
        return final