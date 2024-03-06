class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_we(_sum, i, cap, day):
            if day == 0:
                return False
            if i == len(weights) - 1 and _sum + weights[i] <= cap:
                return True
            if i == len(weights):
                return False
            # else:
            #     return False
            _sum += weights[i]
            # print(_sum)
            if _sum > cap:
                return can_we(0, i, cap, day - 1)
            return can_we(_sum, i + 1, cap, day)
        _max = 0
        _min = -float('inf')
        for i in weights:
            _max += i
            _min = max(_min, i)
        # print(_max, _min)
        # print(can_we(0, 0, 15, days))
        ans = float('inf')
        while _min <= _max:
            mid = _min + (_max - _min) // 2
            if can_we(0, 0, mid, days):
                ans = min(ans, mid)
                _max = mid - 1
            else:
                _min = mid + 1

        # print(ans)
        return ans