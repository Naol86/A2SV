class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        count = 0
        leng = len(nums)
        for i in range(leng):
            for j in range(i + 1, leng):
                if nums[i] + nums[j] < target:
                    count += 1
        return count