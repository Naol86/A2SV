class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos_num = []
        neg_num = []
        ans = []
        for i in range(len(nums)):
            if nums[i] < 0:
                neg_num.append(nums[i])
            else:
                pos_num.append(nums[i])
        for i in range(len(nums)//2):
            ans.append(pos_num[i])
            ans.append(neg_num[i])
        return ans