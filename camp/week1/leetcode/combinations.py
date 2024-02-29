from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        lis = [i for i in range(1, n + 1)]
        ans = combinations(lis, k)
        final_ans = []
        for i in ans:
            final_ans.append(list(i))
        return final_ans