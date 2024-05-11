# Problem: Best Time to Buy and Sell Stock with Transaction Fee - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cache = {}
        def buy_sell(i, buy):
            if i >= len(prices):
                return 0
            if buy in cache:
                return cache[buy]
            if prices[i] < prices[buy]:
                return buy_sell(i + 1, i)
            if prices[i] - prices[buy] - fee <= 0:
                return buy_sell(i + 1, buy)
            # print(i, buy)
            # temp = 0 if i + 1 >= len(prices) else prices[i+1]
            one = prices[i] - prices[buy] - fee + buy_sell(i + 2, i + 1)
            two = buy_sell(i+1, buy)
            cache[buy] = max(one, two)
            return max(one, two)
        ans = buy_sell(1, 0)
        return ans