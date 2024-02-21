class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        count = 0
        _min = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] <= _min:
                _min = nums[i]
                continue
            count += math.ceil(nums[i] / _min) - 1
            rem = nums[i] % _min
            # print(nums[i], _min , rem)
            if rem != 0:
                _min = nums[i] // math.ceil(nums[i] / _min)
        return count