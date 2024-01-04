class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        a = 0
        z = len(nums) -1
        count = 0
        while a < z:
            if nums[a] + nums[z] == k:
                count+=1
                a+=1
                z-=1
            elif nums[a] + nums[z] > k:
                z-=1
            else:
                a+=1
        return count