class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        leng = len(nums)
        count = 0  
        for i in range(leng-1, 1, -1):
            for j in range(i - 1, 0, -1):
                x = bisect.bisect_right(nums[:j], nums[i])
                y = bisect.bisect_right(nums[:j], nums[i] - nums[j])
                count += x - y
        return count

