# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        a = 0
        z = len(height) - 1
        max = 0
        while a < z:
            min = height[a] if height[a] < height[z] else height[z]
            vol = min * (z - a)
            if vol > max:
                max = vol
            if min == height[a]:
                a+=1
            else:
                z-=1
        return max