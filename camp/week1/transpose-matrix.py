import numpy as np

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        temp = np.array(matrix)
        ans = []
        for i in range(len(matrix[0])):
            ans.append(list(temp[:,i]))
        return ans 