class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        count = 0
        dis = len(set(nums))
        leng = len(nums)
        for i in range(leng):
            temp = set()
            for j in range(i, leng):
                temp.add(nums[j])
                if len(temp) == dis:
                    count += 1
        return count