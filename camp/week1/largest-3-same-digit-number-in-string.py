class Solution:
    def largestGoodInteger(self, num: str) -> str:
        dic = {}
        _max = -1
        for i in range(3):
            if num[i] not in dic:
                dic = {}
                dic[num[i]] = 1
            else:
                dic[num[i]] += 1
                if dic[num[i]] == 3:
                    _max = int(num[i])
        b = 3
        while b < len(num):
            if num[b] in dic:
                dic[num[b]] += 1
                if dic[num[b]] == 3:
                    _max = max(int(num[b]),_max)
            else:
                dic = {}
                dic[num[b]] = 1
            b += 1
        if _max == -1:
            return ""
        ans = str(_max) * 3
        return ans
            