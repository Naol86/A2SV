# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = defaultdict(set)
        def dp(i, _sum):
            if i == len(nums) and _sum == target:
                return 1
            if i >= len(nums):
                return 0
            if (i, _sum) in cache:
                return cache[(i, _sum)]
            for j in range(2):
                if j == 0:
                    x = dp(i + 1, _sum - nums[i])
                else:
                    y = dp(i + 1, _sum + nums[i])
            cache[(i, _sum)] = x + y
            return x + y
        return dp(0, 0)