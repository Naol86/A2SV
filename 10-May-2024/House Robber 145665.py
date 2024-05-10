# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        def take(i):
            if i >= len(nums):
                return 0
            if i in cache:
                return cache[i]
            one = nums[i] + take(i + 2)
            two = take(i + 1)
            ans = max(one, two)
            cache[i] = ans
            return cache[i]
        return take(0)