# Problem: Best Time to Buy and Sell Stock III - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        _min = prices.copy()
        _max = prices.copy()
        for i in range(1, len(prices)):
            _min[i] = min(_min[i-1], _min[i])
            _max[-i - 1] = max(_max[-i], _max[-i-1])

        _min[0] = 0
        _max[-1] = 0
        for i in range(1, len(prices)):
            _min[i] = max(prices[i] - _min[i], _min[i-1])
            _max[-i-1] = max(_max[-i-1] - prices[-i-1], _max[-i])

        ans = _max[0]
        for i in range(len(prices) - 1):
            ans = max(ans, _min[i] + _max[i+1])
        return ans
