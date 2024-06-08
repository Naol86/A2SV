# Problem: N Queens - https://leetcode.com/problems/n-queens/

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for i in range(n)]
        ans = []
        rows = set() # visited rows
        cols = set() # visited cols
        pos_digo = set() # positive digonal which is row + col
        neg_digo = set() # negative digonal which is row - col
        def back_tracking(j):
            if j == n:
                x = [''.join(i) for i in board]
                ans.append(x)
                return
            for i in range(n):
                if j in rows or i in cols or j + i in pos_digo or j - i in neg_digo:
                    continue
                board[j][i] = 'Q'
                rows.add(j)
                cols.add(i)
                pos_digo.add(i + j)
                neg_digo.add(j - i)

                back_tracking(j + 1)

                board[j][i] = '.'
                rows.remove(j)
                cols.remove(i)
                neg_digo.remove(j - i)
                pos_digo.remove(j + i)

        back_tracking(0)
        return ans