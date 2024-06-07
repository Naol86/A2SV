# Problem: Find Greatest Common Divisor of Array - https://leetcode.com/problems/find-greatest-common-divisor-of-array/

class Solution:
    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)

    def findGCD(self, nums: List[int]) -> int:
        a = nums[0]
        b = a
        for num in nums:
            a = min(a, num)
            b = max(b, num)
        return self.gcd(a, b)