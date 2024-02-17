class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        count = 1
        last = points[0][1]
        for x, y in points[1:]:
            if x > last:
                count += 1
                last = y
            else:
                last = min(last, y)
        return count