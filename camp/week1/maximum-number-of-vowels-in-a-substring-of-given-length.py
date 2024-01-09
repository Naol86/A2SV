class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        a = 0
        b = k
        count = 0
        for i in range(k):
            if s[i] in ["a","e","o","i","u"]:
                count += 1
        ans = count
        while b < len(s):
            if s[a] in ["a","e","o","i","u"]:
                count -= 1
            if s[b] in ["a","e","o","i","u"]:
                count += 1
                ans = max(count, ans)
            a+=1
            b+=1
        return ans