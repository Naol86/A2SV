class Solution:
    def totalNQueens(self, n: int) -> int:
        ans = []
        col = []
        nag_digo = [] # r - c
        pos_digo = [] # r + c
        board = [["." ]* n for i in range(n)]

        def back_tracking(r):
            if r == n:
                temp = ["".join(row) for row in board]
                ans.append(temp)
                return

            for c in range(n):
                if c in col or (c + r) in pos_digo or (c - r) in nag_digo:
                    continue

                col.append(c)
                pos_digo.append(c + r)
                nag_digo.append(c - r)
                board[r][c] = "Q"

                back_tracking(r + 1)

                col.remove(c)
                pos_digo.remove(c + r)
                nag_digo.remove(c - r)
                board[r][c] = "."

        back_tracking(0)
        return len(ans)