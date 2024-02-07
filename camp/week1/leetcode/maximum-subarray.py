class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        _max = nums[0]
        pre = nums[0]
        for i in range(1,len(nums)):
            if pre < 0 and nums[i] >= 0:
                pre = nums[i]
            elif nums[i] < 0:
                if  -nums[i] < pre:
                    pre += nums[i]
                else:
                    pre = nums[i]
            else:
                pre += nums[i]
            _max = max(_max, pre)
        return _max