class Solution:
    def find(self, _dict):
        _max = - float('inf')
        for key, value in _dict.items():
            _max = max(value, _max)
        return _max

    def characterReplacement(self, s: str, k: int) -> int:
        _dict = defaultdict(int)
        left = 0
        right = 0
        _max = 0
        leng = len(s)
        while right < leng:
            _dict[s[right]] += 1
            right += 1
            temp = self.find(_dict)
            # print(_dict, s[left:right])
            if (right - left - temp) > k:
                _dict[s[left]] -= 1
                left += 1
            _max = max(_max, right - left)
        return _max