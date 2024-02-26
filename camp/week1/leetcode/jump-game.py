class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def helper(i, jump):
            if i == len(nums) - 1:
                return True
            if jump == 0 and nums[i] == 0:
                return False
            jump = max(jump, nums[i])
            return helper(i + 1, jump - 1)
        return helper(0, nums[0])