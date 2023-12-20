class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dic = {}
        ans = set([])
        leng = len(nums)
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
            if dic[i] > (leng/3):
                ans.add(i)
        return list(ans)