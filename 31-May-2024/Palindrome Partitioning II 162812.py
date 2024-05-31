# Problem: Palindrome Partitioning II - https://leetcode.com/problems/palindrome-partitioning-ii/

class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        palendrome = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    palendrome[i][j] = j - i <= 2 or palendrome[i+1][j-1]
        # for i in palendrome:
        #     print(*i)
        #     print('-------------------')
        @lru_cache(None)
        def dp(l, r):
            if palendrome[l][r]:
                return 0
            ans = sys.maxsize
            for i in range(l, r):
                if palendrome[l][i]:
                    ans = min(ans, 1 + dp(i + 1, r))
            return ans
        ans = dp(0, n - 1)
        return ans