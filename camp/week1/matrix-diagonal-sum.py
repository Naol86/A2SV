class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        leng = len(mat)-1
        _sum = 0
        index = 0
        for i in mat:
            _sum += i[index] + i[leng-index]
            index += 1
        if leng % 2 == 0:
            _sum -= mat[leng//2][leng//2]
        return _sum
