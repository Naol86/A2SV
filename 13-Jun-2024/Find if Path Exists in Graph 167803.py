# Problem: Find if Path Exists in Graph - https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        vertex = defaultdict(list)

        for a, b in edges:
            vertex[a].append(b)
            vertex[b].append(a)
        # print(vertex)
        def find(node):
            if vertex[node] == []:
                return False
            if node == destination:
                return True
            for i in range(len(vertex[node])):
                if vertex[node] == []:
                    break
                temp = find(vertex[node].pop())
                if temp:
                    return True
            return False
        return find(source)