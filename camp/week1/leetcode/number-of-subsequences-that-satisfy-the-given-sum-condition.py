class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        MOD = pow(10, 9) + 7

        count = 0
        left = 0
        while left < len(nums) and nums[left] * 2 <= target:
            right = bisect.bisect_right(nums, target - nums[left])
            count += pow(2, (right - left - 1), MOD) 
            left += 1

        return count % MOD