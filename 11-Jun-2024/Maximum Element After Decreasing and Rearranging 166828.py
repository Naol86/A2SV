# Problem: Maximum Element After Decreasing and Rearranging - https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        arr[0] = 1
        _max = 1
        for i in range(1, len(arr)):
            if abs(arr[i-1] - arr[i]) > 1:
                arr[i] = arr[i-1] + 1
            _max = max(_max, arr[i])
        return _max