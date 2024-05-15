# Problem: Coin Change II - https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}
        def dp(i, left):
            if left == 0:
                return 1
            if left < 0:
                return 0
            if (left, i) in cache:
                return cache[(left, i)]
            _sum = 0
            for j in range(i, len(coins)):
                _sum += dp(j, left - coins[j])
            cache[(left, i)] = _sum
            return _sum
        ans = dp(0, amount)
        # print(cache)
        # print(used)
        return ans