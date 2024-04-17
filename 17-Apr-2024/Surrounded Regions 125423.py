# Problem: Surrounded Regions - https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = len(board)
        col = len(board[0])
        visited = set()
        # queue append O's found at edges
        queue = deque()
        for i in range(len(board[0])):
            if board[0][i] == 'O':
                queue.append((0, i))
                visited.add((0, i))
            if board[-1][i] == 'O' and (len(board)-1, i) not in visited:
                queue.append((len(board)-1, i))
                visited.add((len(board)-1, i))
        for j in range(len(board)):
            if board[j][0] == "O":
                queue.append((j, 0))
                visited.add((j, 0))
            if (j, len(board[0])-1) not in visited and board[j][-1] == 'O':
                queue.append((j, len(board[0])-1))
                visited.add((j, len(board[0])-1))
        pos = [(0,1),(0,-1),(1,0),(-1,0)]
        while queue:
            r, c = queue.popleft()
            for i, j in pos:
                nr = r + i
                nc = c + j
                if nr < 0 or nc < 0 or nr >= row or nc >= col or (nr, nc) in visited:
                    continue
                if board[nr][nc] == 'O':
                    visited.add((nr, nc))
                    queue.append((nr, nc))
        # print(visited)
        for i in range(row):
            for j in range(col):
                if board[i][j] == "O" and (i, j) not in visited:
                    board[i][j] = "X"

                
