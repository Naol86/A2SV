# Problem: Minimize Maximum Pair Sum in Array - https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        left = 0
        right = len(nums) - 1
        ans = 0
        while right > left:
            ans = max(ans, nums[left] + nums[right])
            right -= 1
            left += 1
        return ans