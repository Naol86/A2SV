from collections import Counter
class Solution:
    def minimizedStringLength(self, s: str) -> int:
        dic = Counter(s)
        _max = len(s)
        for i in dic:
            _max = _max - dic[i] + 1
        return _max