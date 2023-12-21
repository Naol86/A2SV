class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic={}
        for i in range(len(nums)):
            difference = target-nums[i]
            if nums[i] not in dic:
                dic[difference]=i
            else:
                ans=[i,dic[nums[i]]]
                ans.sort()
                return ans
        