class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = set()
        temp = []
        candidates.sort()
        def helper(left, pos):
            if left == 0:
                ans.add(tuple(temp))
                return
            visited = set()
            for i in range(pos, len(candidates)):
                if candidates[i] in visited:
                    continue
                if left - candidates[i] >= 0:
                    visited.add(candidates[i])
                    temp.append(candidates[i])
                    helper(left - candidates[i], i + 1)
                    temp.pop()
                else:
                    break

        helper(target, 0)
        final_ans = []
        for num in ans:
            final_ans.append(list(num))
        return final_ans
