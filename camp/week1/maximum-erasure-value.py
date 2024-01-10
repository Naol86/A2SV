class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        double = 0
        _max = 0
        pre = 0
        left = 0
        right = 0
        while right < len(nums):
            if nums[right] not in dic:
                dic[nums[right]] += 1
                pre += nums[right]
                _max = max(_max, pre)
                right += 1
            else:
                dic.pop(nums[left])
                pre -= nums[left]
                left += 1
        return _max