# Problem: Pow (x, n) - https://leetcode.com/problems/powx-n/

class Solution:
    def power(self, x, n):
        # print(n)
        if n == 0:
            return 1
        if n == 1:
            return x
        temp = self.power(x, n//2)
        if n % 2 == 1:
            return temp * temp * x
        return temp * temp
    def myPow(self, x: float, n: int) -> float:

        ans = self.power(x, abs(n))
        if n < 0:
            return 1/ans
        return ans