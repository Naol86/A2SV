class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pro = 1
        zero = 0
        for i in nums:
            if i == 0:
                zero += 1
            else:
                pro *= i
        for i in range(len(nums)):
            if zero > 1 or (nums[i] != 0 and zero > 0):
                nums[i] = 0
            elif nums[i] == 0 and zero == 1:
                nums[i] = pro
            else:
                nums[i] = pro // nums[i]
        return nums
