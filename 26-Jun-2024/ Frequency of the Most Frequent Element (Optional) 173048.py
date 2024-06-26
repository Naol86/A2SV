# Problem:  Frequency of the Most Frequent Element (Optional) - https://leetcode.com/problems/frequency-of-the-most-frequent-element/

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        _sum = 0
        left = right = 0
        _max = 0
        while right < len(nums):
            _sum += nums[right]
            need = (right - left + 1) * nums[right] - _sum
            if need <= k:
                _max = max(_max, right - left + 1)
                right += 1
            elif right == left:
                left += 1
                right += 1
                _sum = 0
            else:
                _sum -= (nums[left] + nums[right])
                left += 1
        return _max


