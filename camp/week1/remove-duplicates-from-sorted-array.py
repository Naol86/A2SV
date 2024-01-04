class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        leng = len(nums)
        check = nums[0]
        point = 1
        i = 1
        while i < leng:
            if nums[i] != check:
                check = nums[i]
                nums[point], nums[i] = nums[i], nums[point]
                point += 1
            i += 1
        return point 