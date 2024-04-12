# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        ans = [-1] * n
        ans[0] = 0
        red_edges = defaultdict(list)
        blue_edges = defaultdict(list)
        for x, y in redEdges:
            red_edges[x].append(y)
        for x, y in blueEdges:
            blue_edges[x].append(y)
        queue = deque([(0, 0, True), (0, 0, False)])
        visited = set()
        # print(red_edges)
        # print(blue_edges)
        while queue:
            leng = len(queue)
            for _ in range(leng):
                node, level, color = queue.popleft()
                if (node, color) in visited:
                    continue
                if color:
                    for i in red_edges[node]:
                        queue.append((i, level + 1, not color))
                        # ans[i] = level + 1
                        if ans[i] == -1:
                            ans[i] = level + 1
                else:
                    for i in blue_edges[node]:
                        queue.append((i, level + 1, not color))
                        if ans[i] == -1:
                            ans[i] = level + 1
                visited.add((node, color))
        return ans
