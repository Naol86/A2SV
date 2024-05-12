# Problem: Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = [0] * len(prices)
        buy[0] = -prices[0]
        sell = [0] * len(prices)
        for i in range(1, len(prices)):
            buy[i] = max(buy[i-1], -prices[i])
            sell[i] = max(sell[i-1], prices[i] + buy[i])
        return sell[-1]