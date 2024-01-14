# from collection import Counter
class Solution:
    def check(self, _dict, target):
        for key, value in _dict.items():
            if value > target:
                return False
        return True

    def balancedString(self, s: str) -> int:
        lis = Counter(s)
        leng = len(s)
        n = leng // 4
        if self.check(lis, n):
            return 0
        _min = float('inf')
        left = 0
        right = 0
        while right < leng:
            lis[s[right]] -= 1
            right += 1
            while self.check(lis, n):
                _min = min(_min, right - left)
                lis[s[left]] += 1
                left += 1
        return _min