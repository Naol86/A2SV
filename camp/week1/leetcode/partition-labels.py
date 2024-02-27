class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        _dict = {}
        for i in range(len(s)):
            _dict[s[i]] = i
        ans = []
        start = -1
        last = _dict[s[0]]
        i = 0
        while i < len(s):
            last = max(last, _dict[s[i]])
            if i == last:
                ans.append(i - start)
                start = i
            i += 1
        return ans