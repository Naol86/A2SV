class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        ans = []
        s = [i for i in s]
        for i in range(len(s)):
            small = set()
            capital = set()
            temp = set()
            for j in range(i, len(s)):
                if s[j].islower():
                    small.add(s[j])
                else:
                    capital.add(s[j])
                temp.add(s[j].upper())
                if len(small) == len(capital) and len(capital) == len(temp):
                    if len(ans) < j - i + 1:
                        ans = s[i:j+1]
        return ''.join(ans)