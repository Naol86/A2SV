class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        _max = 0
        for i in houses:
            left = bisect.bisect_left(heaters, i)
            right = 0
            # print(left, ' ------> ', i)
            if left == len(heaters):
                right = abs(i - heaters[left - 1])
                left = float('inf')
            elif left == 0:
                right = abs(i - heaters[left])
                left = float('inf')
            else:
                right = abs(i - heaters[left])
                left = abs(i - heaters[left - 1])
            _max = max(_max, min(left, right))
            # print(left, right)
        # print(_max)
        return _max
