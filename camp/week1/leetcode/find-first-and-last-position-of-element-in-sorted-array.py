class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = bisect.bisect_left(nums, target)
        right = bisect.bisect_right(nums, target)
        if left == len(nums) or right == 0:
            return [-1, -1]
        if nums[left] != target:
            return [-1, -1]
        return [left, right - 1]