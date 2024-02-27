class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        if n == 1:
            return 5
        if n == 2:
            return 20
        if n % 2 == 0:
            return pow(20, n//2, MOD)
        else:
            return (5 * self.countGoodNumbers(n - 1)) % MOD