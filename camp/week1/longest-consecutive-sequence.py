class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        _max = 0
        nums = list(set(nums))
        nums.sort()
        nums.append(nums[0] - 1)
        print(nums)
        temp = 1
        for i in range(len(nums) - 1):
            if nums[i+1] != nums[i] + 1:
                _max = max(_max, temp)
                temp = 1
                continue
            temp += 1
        return _max
