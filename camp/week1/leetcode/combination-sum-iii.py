class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if n > 45:
            return []

        ans = []
        temp = []
        def helper(left, digits, start):
            if digits == 0:
                if left == 0:
                    ans.append(temp.copy())
                return
            for i in range(start, 10):
                if left - i >= 0:
                    temp.append(i)
                    helper(left - i, digits - 1, i + 1)
                    temp.pop()
        helper(n, k, 1)
        return ans