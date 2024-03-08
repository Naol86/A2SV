class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        candles = []
        ans = []
        for i in range(len(s)):
            if s[i] == '|':
                candles.append(i)
        for left, right in queries:
            l = bisect.bisect_left(candles, left)
            r = bisect.bisect_right(candles, right)

            if l == r:
                ans.append(0)
            else:
                leng = candles[r-1] - candles[l] + 1 - (r - l)
                ans.append(leng)
        return ans