class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        _max = nums[0]
        for i in range(1,len(nums)):
            if nums[i]:
                nums[i] = nums[i] + nums[i - 1]
                _max = max(_max, nums[i])
        return _max