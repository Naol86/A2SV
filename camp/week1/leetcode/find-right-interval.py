class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        for i in range(len(intervals)):
            intervals[i].append(i)
        intervals.sort()
        ans = [-1] * len(intervals)
        # print(intervals)
        for i in range(len(intervals)):
            index = bisect.bisect_left(intervals, [intervals[i][1]])
            if index == len(intervals):
                continue
            ans[intervals[i][2]] = intervals[index][2]
            # print(index)
        return ans