# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = defaultdict(int)
        ans = [float('inf')]
        def dp(co, left):
            if left < 0:
                return float('inf')
            if left == 0:
                ans[0] = min(ans[0], co)
                return 1
            if left in cache:
                ans[0] = min(ans[0], co + cache[left] - 1)
                return cache[left]
            x = float('inf')
            for coin in coins:
                x = min(x,dp(co + 1, left - coin))
            cache[left] = x + 1
            return x + 1
        dp(0,amount)
        if ans[0] == float('inf'):
            return -1
        return ans[0]