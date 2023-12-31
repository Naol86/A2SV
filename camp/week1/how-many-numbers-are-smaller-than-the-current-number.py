class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            co=0
            for j in range(len(nums)):
                if nums[i]>nums[j] and i!=j:
                    co+=1
            ans+=[co]
        return ans
        