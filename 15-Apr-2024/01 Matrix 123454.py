# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = deque()
        row = len(mat)
        col = len(mat[0])
        visited = set()
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 1:
                    continue
                queue.append((i, j, 1)) # i, j, level
                visited.add((i,j))
        # print(queue)
        def helper(i, j, level):
            nonlocal row,col
            pos = [(1,0),(-1,0),(0,1),(0,-1)]
            for x, y in pos:
                new_i = i + x
                new_j = j + y
                if new_i < 0 or new_j < 0 or new_i >= row or new_j >= col or (new_i, new_j) in visited:
                    continue
                # if mat[i][j] == 0:
                    # continue
                mat[new_i][new_j] = level
                queue.append((new_i, new_j, level + 1))
                visited.add((new_i, new_j))
        while queue:
            i, j, level = queue.popleft()
            helper(i, j, level)
            # print(queue)
        return mat