class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        _max = nums[0]
        _sum = nums[0]
        for i in range(1, len(nums)):
            _sum += nums[i]
            if nums[i] > nums[i - 1]:
                _max = max(_max, ceil(_sum / (i + 1)))
                nums[i] = _max
        return _max
