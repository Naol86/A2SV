import numpy as np

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a = 0
        b = len(nums) - 1
        while a < b:
            if nums[a] == 0:
                nums.pop(a)
                nums.append(0)
                b-=1
            else:
                a+=1