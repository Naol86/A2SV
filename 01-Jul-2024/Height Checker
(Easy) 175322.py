# Problem: Height Checker
(Easy) - https://leetcode.com/problems/height-checker/

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        temp = sorted(heights)
        count = 0
        for i in range(len(heights)):
            count += heights[i] != temp[i]
        return count