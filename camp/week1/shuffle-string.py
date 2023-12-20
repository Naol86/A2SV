class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        leng = len(s)
        ans = [0] * leng
        for i in range(leng):
            ans[indices[i]] = s[i]
        return ''.join(ans)