class Solution:
    def __init__(self):
        self.up = True
    def go_up(self, row,col, mat):
        if self.can_we(row - 1, col + 1, mat):
            return [row - 1, col + 1]
        self.up = False
        if self.can_we(row, col + 1, mat):
            return [row, col + 1]
        if self.can_we(row + 1, col, mat):
            return [row + 1, col]
        return []
    def go_down(self, row, col, mat):
        if self.can_we(row + 1, col - 1, mat):
            return [row + 1, col - 1]
        self.up = True
        if self.can_we(row + 1, col, mat):
            return [row + 1, col]
        if self.can_we(row, col + 1, mat):
            return [row, col + 1]
        return []
    def can_we(self, row, col, mat):
        if row < 0 or col < 0:
            return False
        if row >= len(mat) or col >= len(mat[0]):
            return False
        return True
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if len(mat) == 1:
            return mat[0]
        ans_list = []
        row = 0
        col = 0
        while True:
            if self.can_we(row, col, mat):
                ans_list.append(mat[row][col])
            if self.up:
                temp = self.go_up(row, col, mat)
                if len(temp) == 0:
                    return ans_list
                row = temp[0]
                col = temp[1]
            else:
                temp = self.go_down(row, col, mat)
                if len(temp) == 0:
                    return ans_list
                row = temp[0]
                col = temp[1]
        return []