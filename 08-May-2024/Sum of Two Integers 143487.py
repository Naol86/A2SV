# Problem: Sum of Two Integers - https://leetcode.com/problems/sum-of-two-integers/description/

class Solution:
    def getSum(self, a: int, b: int) -> int:
        num1 = abs(a)
        num2 = abs(b)
        def complement(num):
            num ^= ((1<<12) - 1)
            return num + 1
        if a < 0:
            num1 |= (1<<12)
            num1 = complement(num1)
        if b < 0:
            num2 |= (1<<12)
            num2 = complement(num2)
        ans = num1 + num2
        if ans & (1<<12) == 0:
            return  ans & ((1<<13) -1)
        ans -= 1
        ans ^= ((1<<13) - 1)
        ans &= ((1<<13) - 1)
        return -ans
        