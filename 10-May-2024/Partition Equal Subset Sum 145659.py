# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        _sum = [sum(nums)]
        self.check = True
        cache = {}
        def dp(i, partition):
            if not self.check:
                return True
            if (i, partition) in cache:
                return cache[(i, partition)]
            if i >= len(nums) or _sum[0] - partition < partition:
                return False
            if _sum[0] - partition == partition:
                return True
            cache[(i, partition)] = dp(i + 1, partition + nums[i]) or dp(i + 1, partition)
            return cache[(i, partition)]
        return dp(0, 0)