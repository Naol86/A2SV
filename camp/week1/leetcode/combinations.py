class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def helper(lis, cur):
            if len(lis) == k:
                temp = lis.copy()
                ans.append(temp)
                return
            for i in range(cur + 1, n + 1):
                temp = lis.copy()
                temp.append(i)
                helper(temp, i)
        helper([], 0)
        return ans