# Problem: Maximum Performance of a Team - https://leetcode.com/problems/maximum-performance-of-a-team/

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        for i in range(len(speed)):
            efficiency[i] = (efficiency[i], speed[i])
        efficiency.sort(reverse=True)
        heap = []
        ans = 0
        _sum = 0
        for ef, sp in efficiency:
            if len(heap) == k:
                _sum -= heappop(heap)
            _sum += sp
            heappush(heap, sp)
            ans = max(ans, _sum * ef)
        return ans % (10 ** 9 + 7)