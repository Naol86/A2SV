class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        leng = len(s)
        prefix = [0] * (leng + 1)
        for start, end, direction in shifts:
            add = 1 if direction == 1 else -1
            prefix[start] += add
            prefix[end + 1] -= add
        for i in range(1, leng + 1):
            prefix[i] += prefix[i - 1]
        ans = []
        for i in range(leng):
            temp = (ord(s[i]) - 97 + prefix[i]) % 26
            if temp < 0:
                temp = 26 - temp
            ans.append(chr(97 + temp))
        return ''.join(ans)