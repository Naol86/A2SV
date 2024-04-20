# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        outDegree = [[] for _ in range(numCourses)]
        inDegree = [[] for _ in range(numCourses)]
        for i, j in prerequisites:
            outDegree[j].append(i)
            inDegree[i].append(j)
        depend = [len(i) for i in inDegree]
        # print(outDegree)
        # print(inDegree)
        queue = deque()
        ans = []
        for i in range(numCourses):
            if depend[i] == 0:
                queue.append(i)
                ans.append(i)
        # print(depend)
        # print(queue)
        while queue:
            node = queue.popleft()
            for i in outDegree[node]:
                depend[i] -= 1
                if depend[i] == 0:
                    queue.append(i)
                    ans.append(i)
        # print(ans)
        if len(ans) != numCourses:
            return []


        return ans