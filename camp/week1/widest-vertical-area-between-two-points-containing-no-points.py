class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        _max = 0
        for i in range(len(points)-1):
            if points[i+1][0] - points[i][0] > _max:
                _max = points[i+1][0] - points[i][0]
        return _max