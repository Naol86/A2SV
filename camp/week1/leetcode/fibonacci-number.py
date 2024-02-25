class Solution:
    cache = {}
    def fib(self, n: int) -> int:
        if n in self.cache:
            return self.cache[n]
        if n == 1:
            return 1
        elif n == 0:
            return 0
        res = self.fib(n-1) + self.fib(n-2)
        self.cache[n] = res
        return res