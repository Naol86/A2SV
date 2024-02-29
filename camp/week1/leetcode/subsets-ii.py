class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        asd = set()
        def helper(num, cur):
            x = deepcopy(cur)
            x = (i for i in x)
            z = tuple(x)
            # print(z)
            # ans.append(z)
            asd.add(z)
            if num == []:
                return
            for i in range(len(num)):
                temp = deepcopy(cur)
                temp.append(num[i])
                temp_lis = num[i+1:]
                helper(temp_lis, temp)
        nums.sort()
        helper(nums, [])
        for i in asd:
            ans.append(list(i))
        return ans