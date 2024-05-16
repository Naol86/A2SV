# Problem: Integer Break - https://leetcode.com/problems/integer-break/

class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        cache = defaultdict(int)
        def dp(left):
            if left <= 4:
                return left
            if left in cache:
                return cache[left]
            for i in range(2, 5):
                if left - i <= 0:
                    break
                temp = i * dp(left - i)
                cache[left] = max(cache[left], temp)
            return cache[left]
        ans = dp(n)
        # print(cache, ans)
        return ans