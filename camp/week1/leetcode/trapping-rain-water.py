class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_left = height[left]
        max_right = height[right]
        water = 0
        while left <= right:
            if height[right] < height[left]:
                temp = max_right - height[right]
                max_right = max(max_right, height[right])
                right -= 1
            else:
                temp = max_left - height[left]
                max_left = max(max_left, height[left])
                left += 1
            if temp > 0:
                water += temp
        return water