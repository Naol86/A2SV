class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def helper(num, cur):
            x = deepcopy(cur)
            ans.append(x)
            if num == []:
                return
            for i in range(len(num)):
                temp = deepcopy(cur)
                temp.append(num[i])
                temp_lis = num[i+1:]
                helper(temp_lis, temp)
        helper(nums, [])
        return ans
