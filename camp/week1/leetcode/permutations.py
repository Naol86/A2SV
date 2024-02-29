class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def helper(lis, cur):
            # print(lis, cur)
            if lis == []:
                tem = deepcopy(cur)
                ans.append(tem)
                return
            for i in range(len(lis)):
                temp = cur + [lis[i]]
                temp_lis = lis[:i] + lis[i+1:]
                # print(temp_lis, temp, '<-----')
                helper(temp_lis, temp)
        helper(nums, [])
        return ans