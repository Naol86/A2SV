# Problem: Check if There is a Valid Path in a Grid - https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        row = len(grid)
        col = len(grid[0])
        pos = {
            1:{(0,1),(0,-1)},
            2:{(1,0),(-1,0)},
            3:{(0,-1),(1,0)},
            4:{(0,1),(1,0)},
            5:{(0,-1),(-1,0)},
            6:{(-1,0),(0,1)}
        }
        queue = deque([(0,0)])
        visited = set()
        while queue:
            leng = len(queue)
            for _ in range(leng):
                r, c = queue.popleft()
                if r == row - 1 and c == col - 1:
                    return True
                for x, y in pos[grid[r][c]]:
                    new_r, new_c = r + x, c + y
                    if (new_r, new_c) in visited or new_r < 0 or new_r >= row or new_c < 0 or new_c >= col:
                        continue
                    if (-x, -y) not in pos[grid[new_r][new_c]]:
                        continue
                    queue.append((new_r, new_c))
                visited.add((r, c))
        return False

