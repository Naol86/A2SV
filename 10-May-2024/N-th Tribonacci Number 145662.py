# Problem: N-th Tribonacci Number - https://leetcode.com/problems/n-th-tribonacci-number/description/

class Solution:
    cache = {}
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n < 3:
            return 1
        if n in self.cache:
            return self.cache[n]
        x = self.tribonacci(n-3) + self.tribonacci(n-2) + self.tribonacci(n-1)
        self.cache[n] = x
        return x