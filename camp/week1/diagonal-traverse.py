from collections import defaultdict
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        lis = defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                lis[i+j].append(mat[i][j])
        ans = []
        for i in lis:
            if i % 2 == 0:
                ans += lis[i][::-1]
            else:
                ans += lis[i]
        return ans