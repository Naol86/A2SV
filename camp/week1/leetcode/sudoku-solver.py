class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxs = [[set() for i in range(3)] for _ in range(3)]
        for row in range(9):
            for col in range(9):
                if board[row][col] != '.':
                    rows[row].add(int(board[row][col]))
                    cols[col].add(int(board[row][col]))
                    boxs[row//3][col//3].add(int(board[row][col]))
        # print(rows)
        # print(cols)
        # print(boxs)
        def back_tracking(n):
            # print(n)
            if n == 81:
                print(board)
                return True
            row = n // 9
            col = n % 9
            if board[row][col] != '.':
                return back_tracking(n + 1)
            else:
                for i in range(1, 10):
                    if i in rows[row] or i in cols[col] or i in boxs[row//3][col//3]:
                        # n += 1
                        continue
                    # print(row, col, i)
                    board[row][col] = i
                    rows[row].add(i)
                    cols[col].add(i)
                    boxs[row//3][col//3].add(i)

                    x = back_tracking(n + 1)
                    if x:
                        return x

                    board[row][col] = '.'
                    rows[row].remove(i)
                    cols[col].remove(i)
                    boxs[row//3][col//3].remove(i)
            return False

        back_tracking(0)
        for row in range(9):
            for col in range(9):
                board[row][col] = str(board[row][col])
