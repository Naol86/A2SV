# Problem: Longest Arithmetic Subsequence of Given Difference - https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/description/

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dic = defaultdict(int)
        ans = 0
        for i in range(len(arr) - 1, -1, -1):
            dic[arr[i]] = dic[arr[i] + difference] + 1
            ans = max(ans, dic[arr[i]])
            # print(dict(dic))
        return ans