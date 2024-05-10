# Problem: Climbing Stairs - https://leetcode.com/problems/climbing-stairs/

class Solution:
    dp = defaultdict(int)
    def climbStairs(self, n: int) -> int:
        if n in self.dp:
            return self.dp[n]
        elif  n== 0:
            return 1
        elif n < 0:
            return 0
        res = self.climbStairs(n-1) + self.climbStairs(n-2)
        self.dp[n] = res
        return res