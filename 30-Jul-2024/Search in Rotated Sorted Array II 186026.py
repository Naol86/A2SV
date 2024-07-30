# Problem: Search in Rotated Sorted Array II - https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

from collections import deque
class Solution:
    def binary_search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left+right) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False

    def search(self, nums: List[int], target: int) -> bool:
        lis = deque(nums)
        leng = len(nums)
        for i in range(leng-1):
            if nums[i] > nums[i+1]:
                lis.rotate(-(i+1))
                break
        return self.binary_search(lis,target)
        
        