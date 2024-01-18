class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        leng = len(nums)
        if leng == 1:
            return 0
        for i in range(1, leng):
            nums[i] = nums[i - 1] + nums[i]
        if nums[-1] - nums[0] == 0:
            return 0
        point = 1
        while point < leng:
            if nums[point - 1] == nums[-1] - nums[point]:
                return point
            point += 1
        return -1