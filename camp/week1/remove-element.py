class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        leng = len(nums)
        # if leng == 1:
        #     if nums[0] == val:
        #         return 0
        #     return 1
        _sum = leng
        left = 0
        left_1 = 1
        while left_1 < leng:
            if nums[left] != val:
                left += 1
                left_1 += 1
            elif nums[left_1] == val:
                left_1 += 1
            else:
                nums[left], nums[left_1] = nums[left_1],nums[left]
                left += 1
                left_1 += 1
        if leng > left_1 - 1 and nums[left_1 - 1] != val:
            return left + 1
        return left
