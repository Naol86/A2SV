# Problem: Minimum Cost For Tickets - https://leetcode.com/problems/minimum-cost-for-tickets/

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        cache = defaultdict(lambda: float('inf'))
        left = [1, 7, 30]
        def dp(i, end):
            if end > days[-1]:
                return 0
            while i < len(days) and days[i] < end:
                i += 1
            if i in cache:
                return cache[i]
            for j in range(3):
                cache[i] = min(cache[i], costs[j] + dp(i, days[i] + left[j]))
            return cache[i]
        ans = dp(0, days[0])
        # print(cache)
        return ans