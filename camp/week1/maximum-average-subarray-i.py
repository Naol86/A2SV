class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        Max = sum(nums[:k])
        temp = Max
        a = 0
        b = k
        while b < len(nums):
            if temp - nums[a] + nums[b] > Max:
                Max = temp - nums[a] + nums[b]
            temp = temp - nums[a] + nums[b]
            a+=1
            b+=1
        return Max/k
            