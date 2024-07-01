# Problem: Squares of a Sorted Array
(Easy) - https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        lis = []
        leng = len(nums)
        for i in range(leng):
            if nums[i] >= 0:
                break
        neg = i - 1
        pos = i
        while neg >= 0 and pos < leng:
            left = nums[neg] ** 2
            right = nums[pos] ** 2
            if left < right:
                lis.append(left)
                neg -= 1
            else:
                lis.append(right)
                pos += 1
        while neg >= 0:
            lis.append(nums[neg] ** 2)
            neg -= 1
        while pos < leng:
            lis.append(nums[pos] ** 2)
            pos += 1
        return lis