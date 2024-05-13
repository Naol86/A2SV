# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}
        def dp(i, buy):
            if i >= len(prices):
                return 0
            if (i, buy) in cache:
                return cache[(i, buy)]
            temp = buy if prices[buy] <= prices[i] else i
            one = dp(i+1, temp) 
            two = dp(i+2, i + 2) + prices[i] - prices[buy]
            cache[(i, buy)] = max(one, two)
            return max(one, two)
        return dp(0,0)