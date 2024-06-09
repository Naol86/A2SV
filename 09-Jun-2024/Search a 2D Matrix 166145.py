# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        left = 0
        right = row * col - 1
        while left <= right:
            mid = left + (right - left)//2
            r = mid // col
            c = mid % col
            # print(mid, r, c)
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                right = mid - 1
            else:
                left = mid + 1
            # print(left, right)
        return False