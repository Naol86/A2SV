class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        a=0
        b=0
        while b<len(nums):
            if nums[b] == 1 and k >= 0:
                b+=1
            elif nums[b] == 0 and k > 0:
                b+=1
                k-=1
            else:
                if nums[a] == 0:
                    k+=1
                if nums[b] == 0:
                    k-=1
                a+=1
                b+=1
        return b - a