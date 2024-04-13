# Problem: Trapping Rain Water - https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: List[int]) -> int:
        left = [-1]
        right = [-1]
        _max = height[0]
        for i in range(1, len(height)):
            left.append(_max)
            _max = max(_max, height[i])
        _max = height[-1]
        for i in range(len(height) - 2, -1, -1):
            right.append(_max)
            _max = max(_max, height[i])
        right = right[::-1]
        # print(left)
        # print(right)
        ans = 0
        for i in range(len(height)):
            _min = min(left[i], right[i])
            _min -= height[i]
            if _min > 0:
                ans += _min
        return ans