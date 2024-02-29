class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def helper(cur, val):
            if val > target:
                return
            if val == target:
                temp = deepcopy(cur)
                ans.append(temp)
                return
            for i in range(len(candidates)):
                temp = deepcopy(cur)
                temp.append(candidates[i])
                helper(temp, val + candidates[i])
        helper([], 0)
        temp = set()
        for i in ans:
            t = sorted(i)
            temp.add(tuple(t))
        final_ans = []
        for i in temp:
            final_ans.append(list(i))
        # print(temp)
        return final_ans