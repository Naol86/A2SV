# Problem: Minimum Difference Between Largest and Smallest Value in 3 Moves - https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        nums.sort()
        def dfs(l, r, k):
            if k == 0:
                return nums[r] - nums[l]
            left = dfs(l + 1, r, k - 1)
            right = dfs(l, r - 1, k - 1)
            return min(left, right)
        
        return dfs(0, len(nums) - 1, 3)