class Solution:
    def maxScore(self, s: str) -> int:
        left = 1 - int(s[0])
        right = 0
        leng = len(s)
        for i in range(1,leng):
            right+= int(s[i])
        _max = left + right
        for i in range(1,leng-1):
            if s[i] == '1':
                right -= 1
            else:
                left += 1
                _max = max(_max, left + right)
        return _max