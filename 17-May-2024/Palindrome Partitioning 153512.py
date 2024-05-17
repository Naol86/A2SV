# Problem: Palindrome Partitioning - https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        cache = {}
        def check(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        def dp(left):
            if left == len(s) - 1:
                return [s[-1]]
            if left in cache:
                return cache[left]
            ans = []
            for i in range(left, len(s)):
                if check(left, i):
                    tem = [s[left:i + 1]]
                    temp = dp(i + 1)
                    for lis in temp:
                        x = tem.copy()
                        x.extend(lis)
                        ans.append(x)
                    if not temp:
                        ans.append(tem)
                    
                
            cache[left] = ans
            return ans
        return dp(0)