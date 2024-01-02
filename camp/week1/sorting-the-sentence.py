class Solution:
    def sortSentence(self, s: str) -> str:
        lis = s.split()
        ans = [0] * len(lis)
        for i in lis:
            ans[int(i[-1]) - 1] = i[:-1]
        return " ".join(ans)